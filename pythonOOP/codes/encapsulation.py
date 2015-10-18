#! /usr/bin/env python 

class Encapsulation:
    def __init__(self):
        self.var = 1    # OK to access directly
        self._var = 2   # should be considered private
        self.__var = 3  # considered private, name mangled
    def public(self):
    	print "This is public method"
    def _non_public(self):
    	print "This is non-public but still can be accessed"	
    def __private(self):
    	print "This is private method"
   


obj = Encapsulation()

print "public modifer using obj.var: ", obj.var
print "non-public modifer using obj._var: ", obj._var
print "private modifer in python using name mangling which can accessed: ",  obj._Encapsulation__var
#print "private modifer can not access directly using obj.__var and getting an error: ", obj.__var

obj.public()
obj._non_public()
obj._Encapsulation__private()
obj.__private()
