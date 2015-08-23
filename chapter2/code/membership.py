#! /usr/bin/env python 

# membership example 

database = [
	['pantho', '1'],
	['tanvir', '2'],
	['ahmed', '3'],
	['panthotanvir', '4']
]


username = raw_input('User name: ')
password = raw_input('password: ')

if [username, password] in database: print 'User Found'