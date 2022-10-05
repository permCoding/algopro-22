'''
tab = [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]
'''

count_rows, count_cols = 4, 5 
tab = []
for row in range(1, count_rows+1):
    one_row = []
    for col in range(1, count_cols+1):
        one_row.append(row*col)
    tab.append(one_row)
for row in tab:
    print(*row)

# lst = []
# lst.append([123,343,454])
# lst += [123]
# print(lst)
