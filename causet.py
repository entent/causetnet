import numpy as np


def causDiam(n, d = 2, c = 0): #creates a d-dim causal diamond with n elements and curvature c
    X = np.random.rand(2, n) #sprinling points uniformly on a square
    rot = np.array([[1,1],[-1,1]]) #a rotation matrix
    X = np.dot(rot, X) #rotating the sprinkled square to a causal diamond
    
    #creating the causal matrix, 
    #meaning that entries for points that are causally related (past to future) 
    #will have value 1, else 0
    
    X0 = X[0, :].reshape(n, 1)
    xDict = {}
    for i in range(d):
        xDict['X' + str(i)] = X[i, :].reshape(n, 1) - X[i, :].reshape(1, n)
    
    ds2 = -X0**2
    for i in range(1, d):
        ds2 = ds2 + xDict['X' + str(i)]**2

    #a masking matrix to keep only entries for causal matrix elements preceding each other
    mask = (X0 < X0.T)
    causalMat = (ds2 <= 0)
    causalMat = causalmat * mask

    return causalMat.astype(int)
