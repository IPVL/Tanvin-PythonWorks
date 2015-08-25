#! /usr/bin/env python

# Introduction of function, define a function like def 
def hello(name):
	'this statement is for doc string example'
	print "Function body", name

hello.__doc__
hello(name = 'started in Python') 	