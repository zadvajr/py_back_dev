#One way to deal with empty cells is to remove the the row that contains them, since most a times data sets tend to be large, removing some rows won't have huge impacts on your result.
from pandas import read_csv

df = read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())

#end
