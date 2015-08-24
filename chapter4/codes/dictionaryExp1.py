#! /usr/bin/env python

# another example of dictionary

template = '''<html>
				<head><title>%(title)s</title></head>
				<body>
					<h1>%(title)s</h1>
					<p>%(text)s</p>
				</body>'''

data = {'title': 'My Home Page', 'text': 'Welcome to my python World!'}

print template % data