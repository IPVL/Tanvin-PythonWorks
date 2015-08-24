#! /usr/bin/env python

# example of various methods of dictionary 
from copy import deepcopy

# example of shallow copy
database = {'user' :'admin', 'power' : ['read', 'write', 'edit']}

database2 = database.copy()
databaseDeep = deepcopy(database)
database2['user'] = 'general'
database2['power'].remove('edit')

print 'shallow copy database: ', database
print 'modified database: ', database2
print 'deep copy database', databaseDeep

# example of has_key
print 'has_key works: ',databaseDeep.has_key('power')

# example of items ans iteritems
print 'items function :', databaseDeep.items()

temp = databaseDeep.iteritems()

print 'what is iteritems return?? : ', temp
print 'using list operator, iteritems: ', list(temp)

# example of update
updateData = {'user' : 'facebook user'}
databaseDeep.update(updateData)

print 'updated databaseDeep: ', databaseDeep

# example of values 
print 'values in databaseDeep: ', databaseDeep.values()

# example of pop and popitem
print 'pop an item: ', databaseDeep.pop('user')
print 'remaining databaseDeep after pop: ', databaseDeep
print 'pop an item: ', databaseDeep.popitem()
print 'remaining databaseDeep after pop: ', databaseDeep