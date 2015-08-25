#! /usr/bin/env python

# example of while 


while True:
	name = raw_input('Enter your name ->')
	if name.endswith('Gumby') and len(name) > 0:
		if name.startswith('Mr.'):
			print 'Hello, Mr. Gumby'
		elif name.startswith('Mrs.'):
			print 'Hello, Mrs. Gumby'
		else:
			print 'Hello, Gumby'
	else:
		print 'Try again'