#Plottig x and y points
#plot() function used to draw points(markers) in a diagram by default it draws line from point to point
#the function takes parameters to specify points in a diagram
#parameter 1 is an array containing x-axis points
#parameter 2 is an array containing points on y-axis
#for example, to plot a line from (1,3) to (8,10) we have to pass two arrays [1,8] and [3,10] to the plot function

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints, ypoints)
plt.show()

#end
