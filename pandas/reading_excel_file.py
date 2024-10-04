#Reading Excel file into pandas dataframe - using read_excel
from pandas import read_excel

df = read_excel('data.xlsx', sheet_name='data')

print(df.to_string())

#end
