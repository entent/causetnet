import matplotlib.pyplot as plt
import numpy as np
import causet as cs



#the output of causal diamond generating function

d = 3
c, t, x = cs.causDiam(1000, d)
norm = np.linalg.norm(x, axis=0)
x = x/norm # ensuring all spatial points lie on a unit sphere
angle = 1 #1 means angle phi on the x-y plane, 2 means angle theta with z axis

#counting the number of points along the desired angle 
count = np.zeros((2,1000))
for i in range(1000):
    count[0, i] = i+1

# calculating the angles phi and theta
phi = np.zeros((1000,))
for i in range(1000):
    if x[1, i] >= 0:
        phi[i] = np.arccos(x[0, i]/np.sqrt(x[0, i]**2 + x[1, i]**2))
    else:
        phi[i] = -np.arccos(x[0, i]/np.sqrt(x[0, i]**2 + x[1, i]**2))

theta = np.zeros((1000,))
if d > 3:
    theta = np.arccos(x[2])

phi.sort()
theta.sort()


#the predicted number of points with angle 
predNum = np.zeros((1000,))
if angle == 1: 
    predNum = 1000*(phi + np.pi) / (2*np.pi)
else:
    predNum = 1000*(1 - np.cos(theta)) / 2

if angle == 1:
    plt.plot(phi, count[0], 'b-', phi, predNum, 'r-')
    plt.title('Number of points, and number of predicted points with phi')
else:
    plt.plot(theta, count[0], 'b-', theta, predNum, 'r-')
    plt.title('Number of points, and number of predicted points with theta')


#plt.savefig("test.png")
plt.show()
