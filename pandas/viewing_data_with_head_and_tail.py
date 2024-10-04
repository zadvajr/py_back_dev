# Get a quick overview of data with head() and tail() method
#the head() returns the headers and a specified number of rows
#while the tail() returns the tail and some rows
#if the number of rows are not specified in both cases, the head() will return the first 5 rows and the tail() will return the last 5 rows

from pandas import read_csv

df = read_csv("data.csv")

print(df.head(10))

print(df.tail(10))

#end
