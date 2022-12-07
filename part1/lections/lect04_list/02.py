lst = []

lst.append(1)
print(lst)

lst.extend([3,4,5,7])
print(lst)

lst = [123] + lst
lst += [444,555]
print(lst)
