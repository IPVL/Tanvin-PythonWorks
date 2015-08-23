#! /usr/bin/env python 

# list operation like assignation and deletion using slicing

names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl', 'tanvir']
address = ['dhaka', 'sylhet', 'rangpur', 'khulna', 'barisal']

# Assign  in names 
names[1] = 'pantho'
names[4] = 'abdullah'

# After assignation
print names

# delete Alice 
del names[0]

# After deletion
print names

# append tanvir
names.append('tanvir');


# After append
print names

# count tanvir
print "Count frequency of tanvir: ", names.count('tanvir')

# extend with address 
names.extend(address)

# After extend
print names

# index checking 
print names.index('pantho')

# insert in names
names.insert(3, 'ahmed')

# After insertion
print names

# pop in general and index based
names.pop()
names.pop(1)

# After pop 
print names

# remove Beth
names.remove('tanvir')

# After remove
print names

# Reverse list 
names.reverse();

# After reverse 
print names