from random import randint as ri


def get_list_rnd(count):
    return [ri(1, 100) for _ in range(count)]


def sort_select(arr):
    for n in range(len(arr), 0, -1):
        ind_max = 0
        for i in range(n):
            if arr[i] > arr[ind_max]:
                ind_max = i
        arr[ind_max], arr[n-1] = arr[n-1], arr[ind_max]
    return arr


# [ 1, 4, 0, 9, 2, 1, 3, 5 ]
