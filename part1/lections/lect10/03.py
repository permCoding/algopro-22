def get_ariphm(num):
    res = 0
    while num > 0:
        res += num % 10
        num //= 10
    return res


def get_str(num):
    num_str = str(num)
    res = 0
    for smb in num_str:
        res += int(smb)
    return res


def get_map(num):
    return sum(map(int, str(num)))
    

num = 123045
print(get_ariphm(num))
print(get_str(num))
print(get_map(num))
