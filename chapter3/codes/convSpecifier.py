#! /usr/bin/env python

# String conversion specifier example 
from math import pi


format = 'Welcome to %s world, But Why so %s'
values = ('python', 'serious')

print format % values

# another example 


formation = "Pi with three decimals: %.3f"
print formation % pi