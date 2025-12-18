import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([35,25,25,15])
myLabels=(["Apples","Bananas","Cherries","Dates"])
mycolors =["black","hotpink","blue","#4CAF50"]

plt.pie(ypoints, labels=myLabels, colors=mycolors)
plt.show()