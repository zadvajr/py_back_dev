#Higher Dimensional array - you can create an array of any dimension by specifying the dimension using the ndim at creation

import numpy as np 

arr = np.array([1,2,3], ndmin=5)

print(arr)
print("Dimension of the arr is = ", arr.ndim)

#end
