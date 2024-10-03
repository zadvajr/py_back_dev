#Load files to dataframe, if your data sets are stored in a file, pandas can load it into dataframe. files such as csv and json
from pandas import read_csv

df = read_csv("data.csv")

print(df)

#end
