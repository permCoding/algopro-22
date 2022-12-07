def A():
    pass


def B():
    pass


def get_name_func(file_name, pref='def '):
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        filtred = [line for line in lines if line.startswith(pref)]
        names = [line[4:line.find('(')] for line in filtred]
    return names


name_funcs = get_name_func('./03.py')
print(name_funcs)
# for name in name_funcs:
#     print(name)
