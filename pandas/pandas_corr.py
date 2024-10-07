#Determining relationships with corr() method

from pandas import read_csv

df = read_csv("data.csv")

print(df.corr())

#end
