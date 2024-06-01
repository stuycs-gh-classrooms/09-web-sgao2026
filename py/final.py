#! /usr/bin/python
print('Content-type: text/html\n')

import cgitb
cgitb.enable()
import cgi
from pprint import pprint

f = open('data.txt', encoding='utf-8')
file = f.read()
f.close()

year_popular = {'year': [{'title': {'author': '', 'series': '', 'words': {}, 'chars': {}}}]}
years = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

# cleaning file
file = file.strip()
file = file[1:].split('\n\n')
n = 0
while n < len(file):
    file[n] = file[n].split('\n')
    n += 1
    
# creating dictionary
for top3 in file:
    entry = []
    n = 0
    while n < len(top3):
        info = top3[n].split('; ')
        d = {info[0]: {'author': info[1], 'series': info[2], 'words': {}, 'chars': {}}}
        entry.append(d)
        n += 1
        
    year = '20' + years[file.index(top3)]
    year_popular[year] = entry
# pprint(year_popular)

def generate_page(title, body):
	html_header = """<!DOCTYPE html>
<html lang="en">
	<head>
	<meta charset='utf-8'>
	<title>""" + title + """</title>
	<link href="../final/mystyle.css" rel="stylesheet">
	</head>
	<body>\n"""
	html_footer = """	</body>
</html>"""

	print(html_header, body, html_footer)
def p(s):
	return '<p>' + s + '</p>\n'
def h1(s):
	return '<h1>' + s + '</h1>\n'
def list_ (g):
	n = 0
	series = '<ul>\n'
	while n < len(g):
		series += '<li>' + g[n] + '</li>\n'
		n += 1
	return series + '</ul>\n'
def link(s, name):
    return '<a href=' + s + '>' + name + '</a>'

data = cgi.FieldStorage()
request = ''
if ('request' in data):
	request = data['request'].value