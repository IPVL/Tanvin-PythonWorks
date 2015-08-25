#! /usr/bin/env python

# example of enumerate in for loop
strings =['Wecome','to','python']
for index, string in enumerate(strings):
	if 'o' in string:
		strings[index] = 'XWX'
print strings