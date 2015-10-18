#! /usr/bin/env python

class A:
  def save(self): 
     print "A.save"

class B(A): pass

class C(A):
  def save(self): 
     print "C.save"

class D(B, C): pass
 
obj = D()
obj.save()
