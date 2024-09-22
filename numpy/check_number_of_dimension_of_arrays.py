#Check number of dimension of an array - numpy has a method called ndim() that checks the number of dimension of an array

import numpy as np

a = np.array([42])
b = np.array([1,2,3,4])
c = np.array([[1,2,3,4], [5,6,7,8]])
d = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#end
