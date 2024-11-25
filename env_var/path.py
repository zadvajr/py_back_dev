#There is a PATH ENV VAR that is used by OS to find a program to run
# on linux and mac os it is separated by :
# on windows it is separated by ;
import os

path = export PATH
my_path_env = os.getenv(PATH)
                        
print(my_path_env)