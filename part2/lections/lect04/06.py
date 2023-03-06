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


def get_filtred(links, ext='.pdf'):
    return list(filter(lambda e: e[-4:]==ext, links))
    

def write_txt(filename, lines):
    with open(filename, 'w', encoding='utf8') as f:
        f.write('\n'.join(lines))


url = "https://pcoding.ru/darkNet.php"

html = get_html(url)
links = get_links(html)
filtred = get_filtred(links, '.pdf')
write_txt('filtred.txt', filtred)

"""
- доделать чтобы сохранялись ещё и названия документов
<a class="links" href="https://pcoding.ru/pdf/CourseProject.pdf" target="_blank">
    CourseProject.pdf
</a>

пример сохранения:
id;name;ref
1;CourseProject.pdf;https://pcoding.ru/pdf/CourseProject.pdf
...
"""
