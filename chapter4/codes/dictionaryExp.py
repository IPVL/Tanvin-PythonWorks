#! /usr/bin/env python 



# Dictionary example

people = {
		
		'Alice': {
		'phone': '2341',
		'addr': 'Foo drive 23'
		},
		'Beth': {
		'phone': '9102',
		'addr': 'Bar street 42'
		},
		'Cecil': {
		'phone': '3158',
		'addr': 'Baz avenue 90'
		}
	}

labels = {
	'phone': 'phone number',
	'addr': 'address'
}

# get input from user
name = raw_input('Enter Name: ')


request = raw_input('Phone number (p) or address (a)? ')


if request == 'p': 
	key = 'phone'
if request == 'a': 
	key = 'addr'

# get function using in this section	
print "details using get:", people.get(name)

if name in people: 
	print "%s's %s is %s." % (name, labels[key], people[name][key])