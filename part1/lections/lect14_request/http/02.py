def ex_00():
    url = './'
    file_name = '02.py'
    with open(url+file_name, 'r', encoding='utf-8') as f:
        txt = f.readline()
        txt = f.readline()
        txt = f.readline()
    return txt.strip()


def ex_01():
    url = './'
    file_name = '02.py'
    with open(url+file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return [line.strip('\n') for line in lines]


txt = ex_01()
for line in txt:
    print(line)
