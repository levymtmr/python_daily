'''
Create, save and load array with float points.
'''

from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))

print('floats: ', floats[-1])

fp = open('floats.txt', 'wb')
floats.tofile(fp)
fp.close()

floats2 = array('d')
fp = open('floats.txt', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()

print('floats2: ', floats2[-1])

print('floats == floats2: ', floats == floats2)