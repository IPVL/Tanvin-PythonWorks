#! /usr/bin/env python

# example of for loop in advance

# example of parallel iteration
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]

for i in range(len(names)):
	print names[i], 'is', ages[i], 'years old' 

# parallel iteration is the built-in function zip
print "using zip:", zip(names, ages)

for name, age in zip(names, ages):
	print name, 'is', age, 'years old'	

# example of numbered iteration
index = 0
for string in names:
	if 'n' in string:
		names[index] = '[censored]'
		index += 1

print "final values of names:", names