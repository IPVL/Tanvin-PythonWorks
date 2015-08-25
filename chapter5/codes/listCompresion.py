#! /usr/bin/env python

# example of list compression

print "Result of [x*x for x in range(10)]:", [x*x for x in range(10)]

print "Result of [x*x for x in range(10) if x % 3 == 0]:", [x*x for x in range(10) if x % 3 == 0]

# add more for parts
print "Result of [(x, y) for x in range(3) for y in range(3)]:", [(x, y) for x in range(3) for y in range(3)]
