s = """1532154 2 312 31 {{arg:88}} uwewekjwe we w
we w fw fws sd fsd fsdfcs sd{{val:100}} jjvdhgava
{{log:qwerty}}{{pas:123456}}"""

a, b, tag = '{{', '}}', 'log'
pos = 0
posa = s.find(a, pos) + len(a)
posb = s.find(b, posa)
arg = int(s[posa: posb].split(':')[1])
print(arg)
