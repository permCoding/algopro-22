from parsing import get_html as gh


url = 'https://www.championat.com/hockey/_superleague/tournament/5077/table/#all'
html = gh(url)

pos = 0
a, b = '<table ', '</table>'
posa = html.find(a, pos) + len(a)
posb = html.find(b, posa)
table = html[posa: posb]

with open('table.html', 'w', encoding='utf8') as f:
    f.write(table)

trs = []
pos = 0
a, b = '<tr>', '</tr>'
while table.find(a, pos) > -1:
    posa = table.find(a, pos) + len(a)
    posb = table.find(b, posa)
    trs.append(table[posa: posb])
    pos = posb

row = trs[1]
# print(row)
pos = 0
a, b = '<td ', '</td>'
posa = row.find(a, pos) + len(a)
posa = row.find('>', posa) + 1
posb = row.find(b, posa)
print(row[posa: posb].strip())


