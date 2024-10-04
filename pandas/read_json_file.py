#Reading/loading json file into datatframe
from pandas import read_json

df = read_json('data.json')

print(df.to_string())

#end
