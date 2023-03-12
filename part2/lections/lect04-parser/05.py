import requests


def get_html(url):
    ua = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"    
    }
    obr = requests.get(url, headers=ua)
    obr.encoding = "utf8"
    return obr.text


def get_link(html, pos=0):
    a, b = '<a class="links" href="', '" target='
    posa = html.find(a, pos) + len(a)
    posb = html.find(b, posa)
    return html[posa: posb]  # https://pcoding.ru/pdf/AgroRobot.pdf


def get_links(html):
    lst = []
    a, b = '<a class="links" href="', '" target='
    pos = 0
    while html.find(a, pos) > -1:
        posa = html.find(a, pos) + len(a)
        posb = html.find(b, posa)
        lst.append(html[posa: posb])
        
        pos = posb
    return lst


url = "https://pcoding.ru/darkNet.php"
html = get_html(url)
links = get_links(html)
ext = '.pdf'
filtred = filter(lambda e: e[-4:]==ext, links)

f = open('filtred.txt', 'w', encoding='utf8')
for link in filtred:
    f.write(link + '\n')

"""

"""
