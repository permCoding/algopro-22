line = "a awmb a vfg a ds a xaaa"
print(id(line))
sm = 3
print(line[3])  # addr[0] + 2b * sm

lst = list(line)
print(lst)
print(id(lst))

sm = 3
print(lst[sm])  # addr[0] => addr[1] => addr[2] => addr[3]
lst[sm] = '$'
# (value , addr_next)
print(lst)
