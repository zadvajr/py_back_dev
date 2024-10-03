#Pandas Series - is like a column in a table it holds data of any type and it is a one dimensional array
#creating pandas series from a list

import pandas as pd

age = [18, 21, 22, 23, 34, 36,]

my_series = pd.Series(age, index=[x for x in range(1, (len(age)+1))])

print(my_series)

#end
