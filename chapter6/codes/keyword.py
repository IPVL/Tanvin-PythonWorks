#! /usr/bin/env python

# example of keyword
def hello(greeting, name):
	print '%s, %s!' % (greeting, name)
hello(greeting='Hello', name='world')


# reversing using ** 
def hello_1(greeting='Hello', name='world'):
	print '%s, %s!' % (greeting, name)

params = {'name': 'Sir Robin', 'greeting': 'Well met'}

hello_1(**params)