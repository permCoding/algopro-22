from functools import reduce

numbers = [2,9,3,2,3]

# print(reduce(lambda acc, cur: acc^cur, numbers))

a = numbers[0]
for e in numbers[1:]:
    a ^= e
print(a)

print(reduce(lambda x, y: x ^ y, numbers))

# логические операции
True and True == True  # and or xor
# арифметические операции and or xor => & | ^
# 6(10) => 0110(2)
# 5(10) => 0101(2)
# 0110 & 0101 == 0100
# 0110 | 0101 == 0111
# 0110 ^ 0101 == 0011
# a, b = 6, 5
# print(a & b)
# print(a | b)
# print(a ^ b)

# a, b = 6, 5
# c = a ^ b
# c = c ^ b
# print(c)

# 0101 ^ 0101 == 0

