import numpy

a = numpy.arange(12)
print('Value: {} type: {}'.format(a, type(a)))

print(a.shape)

a.shape = 3, 4
print('matrix 3 x 4: ', a)
print(a[2])
print(a[2, 1])



a.shape = 4, 3
print('matrix 4 x 3: ', a)
print(a[:, 1])

print('transpose \n', a.transpose())

# Load and save 

floats = numpy.loadtxt('floats.txt')
print(floats[3])