#! /usr/bin/python
print('Content-type: text/html\n')

import cgitb
cgitb.enable()
import cgi

year_popular = {'year': [{'title': {'author': '', 'series': '', 'words': {}, 'chars': {}}}]}
years = [00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def generate_page(body):
	html_header = """<!DOCTYPE html>
	<html lang="en">
	<head>
	<meta charset='utf-8'>
	<title>Home</title>
	<link href="../final/mystyle.css" rel="stylesheet">
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
request = ''
if ('request' in data):
	request = data['request'].value

generate_page(p(request))
