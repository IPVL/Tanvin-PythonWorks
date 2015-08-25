#! /usr/bin/env python

# recursion example factorial
def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)

while True:
	val = raw_input('Enter number: ')
	print "result: ", factorial(int(val))