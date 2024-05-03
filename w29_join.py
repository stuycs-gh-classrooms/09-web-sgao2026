def make_csv_string(g):
    g = list(map(lambda a: str(a), g))
    return ','.join(g)
print(make_csv_string([90, 99, 97, 89]))

def make_csv_table(g):
    g = list(map(lambda a: make_csv_string(a), g))
    return '\n'.join(g)
g = [[90, 99, 97, 89], [91, 94, 99, 89], [81, 94, 100, 100], [90, 99, 79, 81], [50, 79, 49, 41], [90, 99, 94, 94]]
print(make_csv_table(g))

def make_html_list(g):
    g = list(map(lambda a: '<li>' + str(a) + '</li>\n', g))
    return '<ul>\n' + ''.join(g) + '</ul>'
print(make_html_list([90, 99, 97, 89]))

def combine_data(s):
    data = ''
    sets = '\n'.split(s)
    sets = list(map(lambda a: a + ': ', sets))
    
    avgs = []
    x = 0
    while x < len(sets):
        n = 0
        inter = sets[x].split()
        while n < len(inter):
            inter[n] = int(inter[n])
            n += 1
        x += 1
        
    avgs = list(map(lambda a: sum(a) / len(a)))