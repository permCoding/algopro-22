import requests


def get_txt(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0"
    }
    return requests.get(url, headers=head).text


def ex_00(url):
    txt = get_txt(url)
    p1 = txt.find('<div class="temperature"')
    p1 = txt.find('>', p1)
    s2 = '</div>'
    p2 = txt.find(s2, p1)
    print(txt[p1+1:p2])


url = 'https://pogoda7.ru/prognoz/gorod701-Russia-Permskiy_kray-Perm/10days/full'
ex_00(url)


'''
<div class="temperature tooltip" title="Текущая температура в Перми: -17.1°C .. -16°C">-17°C</div>
'''
