import matplotlib.pyplot as plt
import numpy as np
import causet as cs



#the output of causal diamond generating function

d = 2
c, t, x = cs.causDiam(1000, d)
r = np.linalg.norm(x, axis = 0)
t= t.reshape((1000,))

plt.plot(r, t, 'bo')


plt.xlabel('r')
plt.ylabel('t')
plt.title('The causal diamond causal set')
#plt.grid(True)
#plt.savefig("test.png")
plt.show()
