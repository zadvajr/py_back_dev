#Load CSV file into dataframe as follows
from pandas import read_csv

df = read_csv('data.csv') #loading data from csv to dataframe

#to print everythig in the file you use .to_string() method
print(df.to_string())

#end
