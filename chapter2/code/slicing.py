#! /usr/bin/env python 

#	slicing operation in list
#	example 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print [8, 9, 10]
print numbers[7:10]

# print [8, 9, 10]
print numbers[7:]

# print [8, 9]
print numbers[7:-1]

# print [8, 9]
print numbers[-3:-1]

# print [1, 2, 3, 4, 5, 6, 7]
print numbers[:-3]

# print [1, 2, 3, 4, 5, 6, 7]
print numbers[:7]

# print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print numbers[:]

# longer step using additional parameter, which is step size

# print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print numbers[0:10:1]

# print [4]
print numbers[3:6:3]

# print [1, 3, 5, 7, 9]
print numbers[0:10:2]


# print [9, 8, 7, 6, 5]
print numbers[8:3:-1]

#	print [10, 8, 6, 4, 2]
print numbers[10:0:-2]

# print []
print numbers[0:10:-2]

# print [10, 8, 6, 4, 2]
print numbers[::-2]

# print [6, 4, 2]
print numbers[5::-2]

# print [10, 8]
print numbers[:5:-2]


#	example 2
url= raw_input("Type an URL what ever you want:")
sliced = url[11:-4]
print "after slicing: ", sliced
sliced = url[-4:]
print "after slicing: ", sliced