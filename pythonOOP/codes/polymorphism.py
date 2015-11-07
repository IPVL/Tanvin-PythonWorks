#! /usr/bin/env python 

__author__ = "Panthotanvir"

class Polymorphism:
    """
	This class is an example of polymorphism  
    """	
    
    def run_account(self, *args):
	"""polymorphism example in method overloading
	"""
	print" ".join(args)

# creating instance of a class, create an object obj of a class Polymorphism
obj = Polymorphism()

# passing parameter to a class
obj.run_account("one")
obj.run_account("one", "two")
obj.run_account("one", "two", "three")


