#! /usr/bin/env python

# example of conditional statement(if, else, else if(elif))


name = raw_input('What is your name? ')
print "length:", len(name)
if name.endswith('Gumby') and len(name) > 0:
	if name.startswith('Mr.'):
		print 'Hello, Mr. Gumby'
	elif name.startswith('Mrs.'):
		print 'Hello, Mrs. Gumby'
	else:
		print 'Hello, Gumby'
else:
	print 'Who are u?'