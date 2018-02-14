import numpy as np
import causet as cs

# generating the data to be used in the training of the autoencoder

# for now we are generating causets in flat space in d dimensions
# later we may incorporate other features such as curvature

tot = 2 #total number of causal sets generated per dimension
n = 100 #total sprinkled points in causet
dims = np.array([2, 3, 4])

data = np.zeros(tot*dims.size, dtype=[('x', 'i4', (n, n)), ('y', 'i4')])
for d in range(dims.size):
    for i in range(tot):
        c, t, x = cs.causDiam(n, dims[d]) 
        data[d*tot + i] = c, dims[d]

np.save('data.npy', data)
