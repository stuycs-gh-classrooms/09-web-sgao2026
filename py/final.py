#! /usr/bin/python
print('Content-type: text/html\n')

import cgitb
cgitb.enable()
import cgi
from pprint import pprint
from matplotlib import pyplot
import io
import base64

# opening data
f = open('../final/data.txt', encoding='utf-8')
file = f.read()
f.close()

year_popular = {'year': {'title': {'author': '', 'series': '', 'rating': ''}}}
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
    entry = {}
    n = 0
    while n < len(top3):
        info = top3[n].split('; ')
        entry[info[0]] = {'author': info[1], 'series': info[2], 'rating': info[3]}
        n += 1
        
    year = '20' + years[file.index(top3)]
    year_popular[year] = entry
year_popular.pop('year')

def generate_page(title, body):
	html = f"""<!DOCTYPE html>
<html lang="en">
	<head>
	<meta charset='utf-8'>
	<title>{title}</title>
	<link href="../final/mystyle.css" rel="stylesheet">
	</head>
	<body>
		<nav>
			<ul>
				<li><a href="../final/final.html">Home</a></li>
				<li><a href="final.py?request=By+Author&search=Submit+Query">By Author</a></li>
				<li><a href="final.py?request=By+Year&search=Submit+Query">By Year</a></li>
			</ul>
		</nav>
		{body}
	</body>
</html>"""

	print(html)
def p(s):
	return f'<p>{s}</p>\n'
def h1(s):
	return f'<h1>{s}</h1>\n'
def list_ (g):
	n = 0
	series = '<ul>\n'
	while n < len(g):
		series += '<li>' + g[n] + '</li>\n'
		n += 1
	return series + '</ul>\n'
def link(s, name):
    return '<a href={s}>{name}</a>'
def make_image_element():
	buffer = io.BytesIO()
	pyplot.savefig(buffer, format="png")
	buffer.seek(0)
	image_code = base64.b64encode(buffer.read()).decode('utf-8')
	src = f"data:image/png;base64,{image_code}"
	return f"<img src={src}>"


data = cgi.FieldStorage()
if (data['request'].value == 'By Author'):
	# generating count of books per author
	counts = {}
	for year in year_popular:
		for book in year_popular[year]:
			if year_popular[year][book]['author'] in counts:
				counts[year_popular[year][book]['author']] += 1
			else:
				counts[year_popular[year][book]['author']] = 1
	pyplot.ylabel('frequency author is in top three')
	pyplot.xlabel('author name')
	if ('graph_type' in data):
		if data['graph_type'] == 'pie':
			pyplot.pie(list(counts.keys()), list(counts.values()))
		else:
			pyplot.bar(list(counts.keys()), list(counts.values()))
	content = make_image_element()
	if ('request' in data):
		title = data['request'].value

page = f"""
<!DOCTYPE html>
<html lang="en">
        <head>
        <meta charset='utf-8'>
        <title>{title}</title>
        <link href="../final/mystyle.css" rel="stylesheet">
        </head>
        <body>
		<nav>
                        <li><a href="../final/final.html">Home</a></li>
                        <li><a href="final.py?request=By+Author&search=Submit+Query">By Author</a></li>
               	        <li><a href="final.py?request=By+Year&search=Submit+Query">By Year</a></li>
                </nav>

		<h1>{title}</h1>
		<p>This is the top three books according to GoodReads {title.lower()}.</p>
		{content}
        </body>
</html>"""
