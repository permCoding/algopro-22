import requests
import json


def get_txt_(url):
    with open('head.json') as f:
        head = json.load(f)
    return requests.get(url).text


def get_txt(url):
    with open('head.json') as f:
        head = json.load(f)
    return requests.get(url, headers=head).text


def ex_00(url):
    txt = get_txt(url)
    txt = get_txt_(url)
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
'''
https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%9F%D0%B5%D1%80%D0%BC%D0%B8

<div id="ArchTemp">
<span class="t_0" style="display: block;">-15 °C</span>
<span class="t_1" style="display: none;">6°F</span></div>
'''