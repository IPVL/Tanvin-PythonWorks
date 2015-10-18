#! /usr/bin/env python 

__author__ = "Panthotanvir"
class Parent(object):    
# Wrap lines so that they dont exceed 79 characters
# Use 4-space indentation, and no tabs.

    def __init__(self):  # construtor declearation 
	""" Constructor delearation """

        print "parent construtor called"

    def override(self):
	   print "container created"

    # Use blank lines to separate functions and classes, and larger blocks of code inside functions.

    def imply(self):  # inheritence example
	   print "swift installed and example of inheritance"

    def alter(self):
        print "parent altered"  

class Child(Parent):
    def __init__(self):  # construtor declearation 
        print "child construtor called"

    def override(self):  # overriding example
	   """ This function is used for overriding and example of docstring  """ 

	   print "account created and example of overriding"

    def alter(self):
       print "Before alter"  
       super(Child,self).alter()  
       print "After alter"


obj = Child()

print "result of isinstance of parent class:", isinstance(obj, Parent)
print "result of isinstance of child class:", isinstance(obj, Child)

print "result of issubclass parent of child", issubclass(Parent, Child)
print "result of issubclass child of parent", issubclass(Child, Parent)

# Actions on the child imply an action on the parent
obj.imply()

# Actions on the child override the action on the parent.
obj.override()

# Actions on the child alter the action on the parent.
obj.alter()

