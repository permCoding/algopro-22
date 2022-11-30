from random import randint as r


def get_flat_list(count, a=0, b=10):
    return [r(a,b) for _ in range(count)]


def get_objs_list(count, a=0, b=10):
    return [(i+1,r(a,b),get_rnd_name()) for i in range(count)]


def get_rnd_name(ln_st=3, ln_fn=12):
    '''
    написать функцию, которая будет возвращать
    случайное имя, генерируемое из списка 
    разрешённых символов случайным образом
    первая буква д/б заглавной
    '''
    symbols = 'абвгде'  # тут создать константу из разрешённых букв
    name = "Светик"  # тут сначала пустая строка
    pass
    pass
    pass
    return name
