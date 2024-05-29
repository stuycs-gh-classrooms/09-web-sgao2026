#! /usr/bin/python
print('Content-type: text/html\n')

from random import random
print ("""<!DOCTYPE html>
	<html lang="en">
		<head>
			<meta charset='utf-8'>
			<title>work 28</title>
		</head>
		<body> 
			<h1> 'generated: '""", random(), """\n</h1></body></html>""")
