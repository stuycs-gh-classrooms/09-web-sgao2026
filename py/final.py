#! /usr/bin/python
print('Content-type: text/html\n')

import cgitb
cgitb.enable()
import cgi

def generate_page(body):
	html_header = """<!DOCTYPE html>
	<html lang="en">
	<head>
	<meta charset='utf-8'>
	<title>Home</title>
	<link href="../final/mystle.css" rel="stylesheet">
	</head>
	<body>\n"""
	html_footer = """</body>
	</html>"""

	print(html_header, body, html_footer)
def p(s):
	return '<p>' + s + '</p>\n'
def h1(s):
	return '<h1>' + s + '</p>\n'
def list_ (g):
	n = 0
	series = '<ul>\n'
	while n < len(g):
		series += '<li>' + g[n] + '</li>\n'
		n += 1
	return series + '</ul>\n'

data = cgi.FieldStorage()
name = ''
if ('name' in data):
	name = data['name'].value
bgcolor = ''
if ('bgcolor' in data):
	bgcolor = data['bgcolor'].value

generate_page(p(name  + ' ' +  bgcolor))
