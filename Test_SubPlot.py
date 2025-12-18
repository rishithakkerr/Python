import matplotlib.pyplot as plt
import numpy as np

xpoints= np.array(["A","B","C","D"])
ypoints = np.array([3,8,1,10])

plt.bar(xpoints, ypoints)
plt.show()