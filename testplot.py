import matplotlib.pyplot as plt
import numpy as np
import causet as cs



#the output of causal diamond generating function

d = 4
c, t, x = cs.causDiam(1000, d)
#X=np.random.rand(2,1000)
#rot=np.array([[1, -1],[1, 1]])/np.sqrt(2)
#X=np.dot(rot, X)
#t=X[0,:]
#x=X[1,:]

#counting the number of points along the t-axis
count = np.zeros((2,1000))
for i in range(1000):
    count[0, i] = i+1

t.sort()
t = t.reshape((1000,))
count[1,:] = t

#the predicted number of points with time (in a causal diamond with spherical diameter)
predNum = np.zeros((1000,))
predNum[t<=0] = 1000*0.5*(t[t<=0]+1.)**d
predNum[t>0] = 1000*(-0.5)*(1.-t[t>0])**d + 1000

plt.plot(count[1], count[0], 'b-', t, predNum, 'r-')

#plt.plot(x, t, 'bo')


plt.xlabel('x')
plt.ylabel('t')
plt.title('Number of points, and number of predicted points with time')
#plt.title('The causal diamond causal set')
#plt.grid(True)
#plt.savefig("test.png")
plt.show()
