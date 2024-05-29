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
generate_page('<p>hiihiihihihihih</p>')
