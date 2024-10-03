#Creating pandas labels with index keyword,
#if nothing else is specified the values are labeled with their index number and could be accessed through same.
#however, there is a better way of doing that using index keyword


fruits = ["Apple", "Banana", "Cherry", "Lemon", "Orange"]

import pandas as pd

my_series = pd.Series(fruits, index=['x', 'y', 'z', 'j', 'k'])

print(my_series)

#you can also access each value by using the index name
print(my_series['x'])  #should print Apple

#end
