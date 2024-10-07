#Pandas Plotting - pandas uses the plot() method you can also specify the type of plot with kind arguments.
#scatter - a scatter plot needs an x and y axis

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
df.plot(kind="scatter", x="Duration", y="Calories")
plt.show()

#end
