import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0, np.pi*4, 0.1)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y)
plt.plot(x,z)
plt.show()

exp = np.exp(x)
l= range(1,10)
log = np.log(l)

plt.plot(x,exp)
plt.show()
plt.plot(l,log)
plt.show()


