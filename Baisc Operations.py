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