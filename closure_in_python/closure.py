#! /usr/bin/env python

def generate_power_func(n):
    print "id(n): %X" % id(n)
    print "entry value of n:", n
    def nth_power(x):
        print "the value of n:", n
	print "the value of x:", x
	print "the value of (power operator) x**n:", x**n
        return x**n
    print "id(nth_power): %X" % id(nth_power)
    # nth_power is called a closure
    return nth_power


raised_to_4 = generate_power_func(4)

#print __closure__ of raised_to_4
print "__closure__: ", raised_to_4.__closure__
# print repy of raised_to_4 
print "Resulting of repr: ", repr(raised_to_4)
# delete generate_power_func
del generate_power_func
# magic of closure in python
raised_to_4(3) 

print "__closure__: ", raised_to_4.__closure__
