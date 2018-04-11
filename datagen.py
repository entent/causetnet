import numpy as np
import causet as cs

# generating the data to be used in the training of the autoencoder

# for now we are generating causets in flat space in d dimensions
# later we may incorporate other features such as curvature

tot_train = 2000 #total number of causal sets (in training set) generated per dimension
tot_test = 500 #total number of causal sets (in test set) generated per dimension
n = 100 #total sprinkled points in causet
dims = np.array([2, 3, 4])

xtrain = np.zeros((tot_train*dims.size, n**2), dtype='int8')
ytrain = np.zeros((tot_train*dims.size, ), dtype='int8')
xtest = np.zeros((tot_test*dims.size, n**2), dtype='int8')
ytest = np.zeros((tot_test*dims.size, ), dtype='int8')

for d in range(dims.size):
    for i in range(tot_train):
        c, t, x = cs.causDiam(n, dims[d]) 
        xtrain[d*tot_train + i] = c.reshape(1, n**2)
        ytrain[d*tot_train + i] = dims[d]
    for i in range(tot_test):
        c, t, x = cs.causDiam(n, dims[d]) 
        xtest[d*tot_test + i] = c.reshape(1, n**2)
        ytest[d*tot_test + i] = dims[d]

np.save('xtrain.npy', xtrain)
np.save('ytrain.npy', ytrain)
np.save('xtest.npy', xtest)
np.save('ytest.npy', ytest)
