s = """1532154 2 312 31 {{     arg:88 
}} uwewekjwe we w
we w fw fws sd fsd fsdfcs sd{{val:100}} jjvdhgava
{{log:qwerty}} {{pas:123456}}"""

a, b = '{{', '}}'
pos = 0
while s.find(a, pos) > -1:
    
    posa = s.find(a, pos) + len(a)
    posb = s.find(b, posa)
    inner = s[posa: posb].strip()
    
    pos = posb
    print(inner)
   