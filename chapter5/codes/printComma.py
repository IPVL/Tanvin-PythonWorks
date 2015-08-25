#! /usr/bin/env python

# importance of comma and print operation's approaches

print 1, 2, 3
print (1, 2, 3)

# adding a comma at the end of print statement
print "Hello",
print "World!" 

# another example of print and comma issues
name ='python'
salutation = 'Mr.'
greeting = 'Hello'

# using multiple statement in a print operation using comma 
print greeting,salutation,name

# comma to express comma as a string in print statement
print greeting,",",salutation,name

# avoid space
print greeting + ",",salutation,name

