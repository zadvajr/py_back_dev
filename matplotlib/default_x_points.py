#Default x-points - if we do not specify the x-axis they will get the default value of 0,1,2,3,4... etc depending on the length of y-axis
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10,5,7])
plt.plot(ypoints)
plt.show()

#end
