#Pandas dataframe is like the entire table of data while the series is just a single column
# you can create dataframes from series.

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}


#load data into dataframe
df = pd.DataFrame(data)

print(df.to_string())

#end
