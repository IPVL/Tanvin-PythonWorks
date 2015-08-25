#! /usr/bin/env python

# example of exec 
exec "print 'Hello, world!'"

# another example 
from math import sqrt
scope = {}
exec 'sqrt = 1' in scope
print "sqrt of 4:", sqrt(4)

print "scope:", scope['sqrt'], '\n', "length of scope:", len(scope)

# example of eval 
eval(raw_input("Enter an arithmetic expression: "))