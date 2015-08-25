#! /usr/bin/env python

# example of deletion using None
scoundrel = {'age': 42, 'first name': 'Robin', 'last name': 'of Locksley'}
robin = scoundrel

print "scoundrel", scoundrel
print "robin", robin

scoundrel = None
print "robin", robin
robin = None
print "robin", robin

# example of del in deletion
x = 1
del x
print "now x:", x