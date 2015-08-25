#! /usr/bin/env python

# example of for loop


words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
	print word,
print '\n'

# example of for loop in dictionary 

d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
	print key, 'corresponds to', d[key]	

# additional sequence unpacking in for loop
for key, value in d.items():
	print key, 'to', value