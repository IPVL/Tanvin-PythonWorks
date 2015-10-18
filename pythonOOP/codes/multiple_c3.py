#! /usr/bin/env python

class A(object):
	def save():
		print "A.save"
class B(object): 
	def save():
		print "B.save"
class X(A, B): pass
class Y(B, A): pass
class Z(X, Y): pass


obj = Z()
obj.save()
