#! /usr/bin/env python 

class Duck:
    """ 
    this class implies a new way to express polymorphism using duck typing. 
    This class has 2 functions: quack() and fly() consisting no parameter.       	 
    """
    def quack(self):
        print("Quack, quack!");

    def fly(self):
        print("Flap, Flap!");


class Person:
    def quack(self):
        print("I'm Quackin'!");

    def fly(self):
        print("I'm Flyin'!");


def in_the_forest(mallard):
    """ This function is used for express polymorphism behavior except inheritance """
    mallard.quack()
    mallard.fly()


 
duck = Duck()
person = Person()

# passing object to in_the_forest() function
in_the_forest(Duck())
in_the_forest(Person())


