from array import array
from random import random

f = open("floats.txt", "w+")

f.write('{}'.format(array('d', (random() for i in range(10**7)))))


# for i in range(10**7):
#     array_float.
#     f.write('{}'.format(i+i*0.3))
    
f.close()