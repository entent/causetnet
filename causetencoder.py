# Using the code from 
# https://github.com/keras-team/keras/blob/master/examples/variational_autoencoder.py being used

import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Input, Dense, Lambda
from keras.models import Model
from keras import backend as K
from keras import metrics

xtrain = np.load('xtrain.npy')
ytrain = np.load('ytrain.npy')
ytest = np.load('ytest.npy')
xtest = np.load('xtest.npy')

trainNoise = 0.05*np.random.rand(xtrain.shape[0], xtrain.shape[1])
testNoise = 0.05*np.random.rand(xtest.shape[0], xtest.shape[1])

xtrain = xtrain.astype('float32') + trainNoise
xtest = xtest.astype('float32') + testNoise

#total_size = data.size #number of training examples
batch_size = 100 #as per example code for now
original_dim = xtrain[0].size
latent_dim = 2 #number of parameters defining the autoencoding (want this number to be small)
intermediate_dim = 1024
epochs = 20
epsilon_std = 1.0

x = Input(shape=(original_dim,))
h = Dense(intermediate_dim, activation='relu')(x)
z_mean = Dense(latent_dim)(h)
z_log_var = Dense(latent_dim)(h)

def sampling(args):
    z_mean, z_log_var = args
# creating some variation on the latent variable to stochastically generate new but similar input
    epsilon = K.random_normal(shape=(K.shape(z_mean)[0], latent_dim), mean=0.,
                              stddev=epsilon_std)
    return z_mean + K.exp(z_log_var / 2) * epsilon

#the latent variable for the decoder is randomly sampled to create an output that is unique but close to the
# input
z = Lambda(sampling, output_shape=(latent_dim,))([z_mean, z_log_var])

#as explained in the source code, these two layers will be used to generate 
#new examples from random values of the latent variable z
decoder_h = Dense(intermediate_dim, activation='relu')
decoder_mean = Dense(original_dim, activation='sigmoid')

h_decoded = decoder_h(z)
x_decoded_mean = decoder_mean(h_decoded)

# the object representing the full autoencoder is defined
vae = Model(x, x_decoded_mean)

#compute VAE loss
# the following loss function is really more for classification problems, 
# but the Keras people seemed to use it successfully for monochrome images, so let's see
xent_loss = original_dim * metrics.binary_crossentropy(x, x_decoded_mean)
# the following weird loss function is explained nicely in comment 4 of 
# http://forums.fast.ai/t/intuition-behind-kl-divergence-regularization-in-vaes/1650/
# basically it is a regularizing cost function to minimize the mean and standard deviation 
# of the encoding in the latent space
kl_loss = - 0.5 * K.sum(1 + z_log_var - K.square(z_mean) - K.exp(z_log_var), axis=-1)
vae_loss = K.mean(xent_loss + kl_loss)


vae.add_loss(vae_loss)
#todo: choose a good optimizer
vae.compile(optimizer='rmsprop')
vae.summary()

#todo: make sure the training and testing data are in the right format

vae.fit(xtrain,
        shuffle=True,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=(xtest, None))

# build a model to project inputs on the latent space
encoder = Model(x, z_mean)


# making a 2D plot of the digit classes in the latent space
x_test_encoded = encoder.predict(xtest, batch_size=batch_size)
plt.figure(figsize=(6, 6))
plt.scatter(x_test_encoded[:, 0], x_test_encoded[:, 1], c=ytest)
plt.colorbar()
plt.show()










