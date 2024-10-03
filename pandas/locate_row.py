#Since dataframe is more like a table, you can use a loc() method to locate a particular row in a table

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}


#load data into dataframe
df = pd.DataFrame(data)

print(df.loc[0]) # will print 420 50

#end
