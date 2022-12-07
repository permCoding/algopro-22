from urllib.request import urlopen


def get_data():
    url = 'https://pcoding.ru/csv/'
    file_name = '01.txt'
    with urlopen(url+file_name) as f:
        txt = f.read().decode('utf-8')
    return txt



print(get_data())
