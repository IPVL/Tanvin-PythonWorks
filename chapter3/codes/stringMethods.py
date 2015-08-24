#! /usr/bin/env python

# implementations of various types of string methods but not all !!!
from string import maketrans


# example of find method
string1 = 'This is a bulshit string containing mistakes, lets find out !'

print string1

print 'Find the mistakes keyword in stirng1 ', string1.find('mistakes')

# example of join
seq = '++'
temp = seq.join(string1)
print temp

# another example of join
dirs = '', 'usr', 'bin', 'env'
seq1= '/'
print seq1.join(dirs)

print 'C:' + '\\'.join(dirs)

# example of lower 
print string1.lower()

#example of replace 
print string1.replace('ul', 'xy')

# example of split 
print temp.split('++')

# example of translate
table = maketrans('is', 'XW')
print string1.translate(table)