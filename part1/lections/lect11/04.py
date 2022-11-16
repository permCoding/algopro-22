lst = [
    ["wew", 2],
    ["qwe", 1],
    ["fgh", 7]
]

lst_s = sorted(lst, key=lambda x: x[1], reverse=True)

for elm in lst_s:
    print(*elm)
