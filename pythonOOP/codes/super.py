#!/usr/bin/env python 

class Apple(object):
    def __init__(self):
        print "init Apple"
   	
class Ball(Apple):
    def __init__(self):
        print "init Ball"
        super(Ball,self).__init__()
    def ap(self):
	print "ball parent"    
class Cat(Ball):
    def __init__(self):
        print "init Cat"
        super(Cat,self).__init__()
    def ap(self):
        print "ball parent"       
class Dog(Cat):
    def __init__(self):
        print "init Dog"
        super(Cat,self).__init__()
    def ap(self):
	super(Dog,self).ap()
	print "dog"	     

    
d = Dog()
d.ap()
