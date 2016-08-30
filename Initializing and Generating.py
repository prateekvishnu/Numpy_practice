import numpy as np

a = np.arange(16).reshape(4,4)
print a
print
print "Properties of A"
print a.ndim
print a.dtype.name
print a.size
print type(a)

b = np.array([6.0, 7.0, 8.0])
print
print b
print "Properties of b"
print type(b)
print b.dtype

c = np.array([(1.5,2,3), (4,5,6)]) #converts all values to float
print c

#complex numbers

d = np.array([[1, 2],[3, 4]],dtype = complex)
print d


#generating arrays

#type 1
e = np.zeros((2,5))
print
print "Type 1"
print "Using Zeros"
print e

#type 2
f = np.ones( (2,3,4), dtype=np.int16 )                # dtype can also be specified
print
print "Type 2"
print "Using Ones"
print f

#type 3
g = np.empty( (2,3) )                                 # uninitialized, output may vary
print
print "Type 3"
print "Using Empty"
print g

#type 4
h = np.arange( 10, 30, 5 )							  #(start inclusive, end not inclusive, increment)
i = np.arange( 0, 2, 0.3 ) 
j = np.arange(16).reshape(4,4)
print
print "Type 4"
print "Using arange"
print h
print
print i
print
print j


#type 5
print 
print "Using linspace"
k = np.linspace( 0, 2, 9 ) 							    #(start inclusive, end not inclusive, no of elements)
print k


#reshape function
print
print "Reshape Function"
l = np.arange(6) 
print "1d array"
print l

print
m = np.arange(12).reshape(3,4)
print "2d array"
print m

print
n = np.arange(24).reshape(2,3,4)
print "3d array"
print n

#If arrays are large Numpy automatically skips the central part of the array and only prints the corners to change this and print entire array uncomment below command.
#np.set_printoptions(threshold='nan')

