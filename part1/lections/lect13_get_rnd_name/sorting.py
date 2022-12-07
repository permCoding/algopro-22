from generator import get_flat_list as gfl


def sort_select(lst, reverse=False):
    for j in range(len(lst)-1):
        ind_max = 0
        for i in range(1, len(lst)-j):
            if lst[i] > lst[ind_max]:
                ind_max = i
        lst[-(j+1)], lst[ind_max] = lst[ind_max], lst[-(j+1)]
    return lst if reverse == False else lst[::-1]


def sort_select_tpl(lst, reverse=False, pos=0):
    for j in range(len(lst)-1):
        ind_max = 0
        for i in range(1, len(lst)-j):
            if lst[i][pos] > lst[ind_max][pos]:
                ind_max = i
        lst[-(j+1)], lst[ind_max] = lst[ind_max], lst[-(j+1)]
    return lst if reverse == False else lst[::-1]


def main():
    lst = gfl(8, 10, 99)
    print(lst)
    print(sort_select(lst))


if __name__ == "__main__":
    print(__name__)
    main()