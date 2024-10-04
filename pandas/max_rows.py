#The number of rows returned by pandas by default is defined in pandas settings option

import pandas as pd

print(pd.options.display.max_rows)

#you can as well change it as follows
pd_max_r = pd.options.display.max_rows = 999

print(pd_max_r)

#end
