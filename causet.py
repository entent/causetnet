import numpy as np

def polar2Cart(theta, phi): 
#given d-3 x n and a 1 x n dim arrays of angles, return a d-1 x n array of cartesian coords
    cosTheta = np.cos(theta); sinTheta = np.sin(theta)
    cosPhi = np.cos(phi); sinPhi = np.sin(phi) 

    d = theta.size[0] + 2; n = theta.size[1]
    x = np.zeros(d-1, n)
    indices = np.arange(d-2)

    for i in range(d-3):
        x[i, :] = np.prod(sinTheta[indices != i, :], axis = 0) * cosTheta[i, :]

#https://tribordo.wordpress.com/2013/06/18/how-to-select-all-rows-except-one-in-python-with-numpy/

    x[d-2, :] = np.prod(sinTheta, axis = 0) * sinPhi
    x[d-1, :] = np.prod(sinTheta, axis = 0) * cosPhi

    return x


def causDiam(n, d = 2, c = 0): #creates a d-dim causal diamond with n elements and curvature c

    t = np.random.rand(1, n) * 2 - 1 #making time go from -1 to 1
    r = np.random.rand(1, n) * np.cos(np.pi * t / 2)
#radial coordinate of spatial slice must not exceed the edge of the diamond
    phi = np.random.rand(1, n) * 2 * np.pi #one angle must go from 0 to 2*pi 
#getting the spatial coordinates in cartesian coords
    x = np.zeros(d-1, n)
    if d == 2:
        x = r * 2 - np.cos(np.pi * t / 2)
    elif d == 3:
        x = np.zeros(2, n)
        x[0, :] = np.cos(phi) * r
        x[1, :] = np.sin(phi) * r
    else:
        theta = np.random.rand(d-3, n) * np.pi #polar coordinates
        x = polar2Cart(theta, phi)
        x = r * x 
    
    #creating the causal matrix, 
    #meaning that entries for points that are causally related (past to future) 
    #will have value 1, else 0
    
    xDict = {}
    xDict['X0'] = t.T - t
    for i in range(1, d):
        xDict['X' + str(i)] = x[i-1, :].reshape(n, 1) - x[i-1, :].reshape(1, n)
    
    ds2 = -xDict['X0']**2
    for i in range(1, d):
        ds2 = ds2 + xDict['X' + str(i)]**2

    #a masking matrix to keep only entries for causal matrix elements preceding each other
    mask = (t.T < t)
    causalMat = (ds2 <= 0)
    causalMat = causalMat * mask

    return causalMat.astype(int)
