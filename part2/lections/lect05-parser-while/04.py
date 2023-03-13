s = """1532154 2 312 31 {{     arg:88 
}} uwewekjwe we w
we w fw fws sd{{arg:103}}  fsd fsdfcs sd{{val:100}} jjvdhgava
{{log:qwerty}} {{pas:123456}} {{arg:-99}} uwewekjwe we w"""

def get_tags(s):
    tags = []
    a, b = '{{', '}}'
    pos = 0
    while s.find(a, pos) > -1:
        posa = s.find(a, pos) + len(a)
        posb = s.find(b, posa)
        inner = s[posa: posb].strip()
        tags.append(inner.split(':'))
        pos = posb
    return tags
    
tags = get_tags(s)
filtred = filter(lambda elm: elm[0]=='arg', tags)
# filtred = 
for tag in filtred:
    print(tag)
   