

#!/usr/local/bin/python3
from numpy  import *

b = arange(12).reshape(4,3) 
print (b)
b[0,0] = 99

print (b)