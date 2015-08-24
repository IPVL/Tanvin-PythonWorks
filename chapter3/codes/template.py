#! /usr/bin/env python 

# template in string

from string import Template

# Template module implemented 

# example 1
string1  = Template('$x, Bangali $x!')

# substitute method 
print string1.substitute(x = 'WoW')

# example 2
string2  = Template('Why so seir${x}s !!!')

# substitute method 
print string2.substitute(x = 'ou')

# example 3
string3 = Template('$first is better $second $third')

add = {}
add['first'] = '1st'
add['second'] = 'than'
add['third'] = '2nd'

print string3.substitute(add)