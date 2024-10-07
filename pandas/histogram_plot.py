#Histogram plot can be specified using the kind of hist

from pandas import read_csv
from matplotlib import pyplot

df = read_csv("data.csv")
df["Duration"].plot(kind="hist")
pyplot.show()

#end
