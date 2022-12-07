from urllib.request import urlopen


def ex_00():
    url = './'
    file_name = '01.py'
    with open(url+file_name, 'r', encoding='utf-8') as f:
        txt = f.read()
    return txt


def ex_01():
    url = 'https://pcoding.ru/csv/'
    file_name = 'abiturs.csv'
    with urlopen(url+file_name) as f:
        txt = f.read().decode('utf-8')
    return txt


def ex_02():
    url = 'https://pcoding.ru/jsprim/sek/js/'
    file_name = 'main.js'
    with urlopen(url+file_name) as f:
        txt = f.read().decode('utf-8')
    return txt


txt = ex_02()
print(txt)
