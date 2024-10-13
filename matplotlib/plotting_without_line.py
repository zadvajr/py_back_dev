#Plotting without a line - to plot only the markers you can use the shortcut parameter 'o' which means rings
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])
plt.plot(xpoints, ypoints, 'o')
plt.show()

#end
