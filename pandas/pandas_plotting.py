#Pandas Plotting - pandas uses the plot() method to creat diagrams
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
df.plot()
plt.show()

#end
