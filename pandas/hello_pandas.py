#My first pandas script

import pandas as pd

my_data_sets = {
            "cars": ["BMW", "Audi", "Toyota", "Lambo"],
            "passings": [3, 7, 8, 9]
        }
myvar = pd.DataFrame(my_data_sets, index=[1,2,3,4])

print(myvar)

#end
