import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0,6,147,234])
ypoints = np.array([0,18,195,250])

# print graph joining points
# plt.plot(xpoints,ypoints, 'o')
# plt.show()

# print points
# plt.plot(xpoints,ypoints, 'o')
# plt.show()

# print points as marker
# plt.plot(xpoints,ypoints, marker = '*')
# plt.show()

# showing dotted lines
plt.plot(xpoints,'o:r')
plt.show()
