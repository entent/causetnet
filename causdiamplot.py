import matplotlib.pyplot as plt
import numpy as np
import causet as cs



#the output of causal diamond generating function

d = 2
c, t, x = cs.causDiam(1000, d)
r = np.linalg.norm(x, axis = 0)
x = x.reshape((1000,))
t= t.reshape((1000,))

plt.plot(x, t, 'bo')


plt.xlabel('x')
plt.ylabel('t')
plt.title('The causal diamond causal set')
plt.axes().set_aspect('equal', 'datalim')
plt.savefig("causaldiamond2d.png")
plt.show()
