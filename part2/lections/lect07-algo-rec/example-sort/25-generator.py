from random import randint, sample


def get_rnd_name(down_=3,up_=12):
    alph = 'абвгдеёжзийклмнопрстуфхцчшщьъэюя'
    count = randint(down_,up_)  # длина фамилии
    return ''.join(sample(alph, k=count)).title()


def get_rnd_records(count=10,down=150,up=250):
    lst = [[i,get_rnd_name(),randint(down,up)] for i in range(1,count+1)]
    return lst


def list_to_file(filename, lst):
    with open(filename, 'w', encoding='utf8') as f:
        for elm in lst:
            f.write(f'{elm[0]},{elm[1]},{elm[2]}\n')


lst = get_rnd_records(100)
list_to_file('abiturs.csv', lst)
