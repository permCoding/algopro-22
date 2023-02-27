f = open("./pcoding.html", 'r', encoding="utf8")
html = f.read()
f.close()

# print(html)

a, b = '<a class="links" href="', '" target='
posa = html.find(a, 0)
posb = html.find(b, posa)
print(html[posa: posb])



"""
<a class="links" href="https://pcoding.ru/pdf/AgroRobot.pdf" target="_blank">
AgroRobot.pdf
</a>
"""