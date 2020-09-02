import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
fig.suptitle("Empty figure")
ax = fig.add_subplot(1,1,1)
ax.set_title('Empty plot')

t = np.array(np.linspace(0, 2, 100))

l = lambda a : 5 * np.sin(2 * np.pi * 1 * a)
h = 3 * np.pi * np.exp(-1 * l(t))

ax.plot(t, h)
plt.show()