from random import randint as r


def get_rnd(count):
    lst = []
    for _ in range(count):
        lst += [r(1, 6)]
    return lst


def check_lst(lst):
    amount = [0] * (6+1)
    for elm in lst:
        amount[elm] += 1
    return amount


lst = get_rnd(6*1000)
# print(lst[0:10])

amount = check_lst(lst)
for i in 1,2,3,4,5,6:
    print(i, amount[i])
