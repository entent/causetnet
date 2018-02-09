import matplotlib.pyplot as plt
import numpy as np
import causet as cs



#the output of causal diamond generating function

d = 2
c, t, x = cs.causDiam(1000, d)

r=np.linalg.norm(x, axis=0) * 1./(1-np.absolute(t))

#counting the number of points along the radial-axis
count = np.zeros((2,1000))
for i in range(1000):
    count[0, i] = i+1

r.sort()
r = r.reshape((1000,))
count[1,:] = r

#the predicted number of points with time (in a causal diamond with spherical diameter)
predNum = 1000*r**(d-1.) 


plt.plot(count[1], count[0], 'b-', r, predNum, 'r-')



plt.xlabel('x')
plt.ylabel('t')
plt.title('Number of points, and number of predicted points with time')
#plt.savefig("test.png")
plt.show()
