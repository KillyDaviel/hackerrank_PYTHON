'''
dot

The dot tool returns the dot product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.dot(A, B)       #Output : 11
cross

The cross tool returns the cross product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.cross(A, B)     #Output : -2
'''

import numpy as np
n=input()
arr1=np.array([list(map(int, input().split())) for _ in range(int(n))])
arr2=np.array([list(map(int, input().split())) for _ in range(int(n))])
print(arr1 @ arr2)

