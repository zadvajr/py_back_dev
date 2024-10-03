#Creating series from dictionary
import pandas as pd

data = {
            "Months": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
            "Days": [31, 28, 31, 30, 31, 30, 31,31,31,31,30,31]
        }
my_data = pd.Series(data)

print(my_data)

#end
