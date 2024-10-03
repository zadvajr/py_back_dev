#with  index argument you can name your own index

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}


#load data into dataframe
df = pd.DataFrame(data, index=["Day 1", "Day 2", "Day 3"])

print(df)

#end
