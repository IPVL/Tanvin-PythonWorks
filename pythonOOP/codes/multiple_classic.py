#! /usr/bin/env python 

# this is an example of classic MRO
class A:
    def save(self): 
        print "A.save" 

class B(A): pass

class C:
    def save(self): 
	print "C.save"

class D(B, C): pass

d = D()
d.save()
