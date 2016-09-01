import numpy as np
a = np.array([20, 50, 70, 40])
b = np.arange(10, 50, 10)
c = a-b
print c

# power of each element
print c**2
#sin fuction
print 10*np.sin(c)
#Returns a bool type array - returns True if value less tha n25 else returns False
print c<25

# Element-wise and Matrix Multiplication

A = np.array( [[1,1], [0,1]] )
B = np.array( [[2,0], [3,4]] )
print "Element wise Multiplication"
print A*B
print

#Matix Multiplication
print "Method 1"
print A.dot(B)
print
print "Method 2"
print np.dot(A,B)

# operations like += and *=

a = np.ones((2,3), dtype=int)
b = np.random.random((2,3))
print "b"
print b

a *= 3
b += a

#a+=b won't work as a is of interger type to do such operations use different variable name eg: c = a+b

# Sum, Min and Max Functions
print
print "sum"
print b.sum()
print "min"
print b.min()
print "max"
print b.max()

#axis parameter
print
print "axis parameter"

c = np.arange(12).reshape(3,4)
print "axis=0 => Coloumn" 
print c.sum(axis=0)

print "axis=1 => Row" 
print c.min(axis=1)

#cumulative sum
print "Cumulative Sum"
print c.cumsum(axis=1)


# Universal Fuctions
d=np.arange(3)
print "exp value of each element"
print np.exp(d)
# Similar functions - exp, sqrt, sin, cos, add
e = np.array([2., -1., 4.])
print "Adding two arrays"
print np.add(d,e)


