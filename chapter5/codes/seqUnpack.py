#! /usr/bin/env python

# example of sequence unpacking 

x, y, z = 1, 2, 3
print x, y, z

# unpacking 
x, y = y, x
print x, y, z

# unpacking 
x, z = y, x
print x, y, z