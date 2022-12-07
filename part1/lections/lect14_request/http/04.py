from urllib.request import urlopen


def get_cities():
    url = 'https://pcoding.ru/csv/'
    file_name = 'abiturs.csv'
    with urlopen(url+file_name) as f:
        txt = f.read().decode('utf-8')
        lines = txt.split('\n')
        names = [line.strip().split(',')[5] for line in lines[1:]]
        result = []
        for name in names:
            if not(name in result):
                result.append(name)
    return result


def get_cities_():
    url = 'https://pcoding.ru/csv/'
    file_name = 'abiturs.csv'
    with urlopen(url+file_name) as f:
        txt = f.read().decode('utf-8')
        lines = txt.split('\n')
        names = [line.strip().split(',')[5] for line in lines[1:]]
        result = list(set(names))
    return result


names = get_cities_()
for name in sorted(names):
    print(name)
