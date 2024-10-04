#view data info with info() method

from pandas import read_csv

df = read_csv('data.csv')

print(df.info())

#end
