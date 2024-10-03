#If you use loc() with a single index it returns a pandas series, but if you use it with list of indexes it returns a pandas dataframe
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into dataframe
df = pd.DataFrame(data) #returns pandas series.
print(df.loc[0])

print(df.loc[[0,1]]) #returns a pandas dataframe

#end
