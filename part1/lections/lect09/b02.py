
line = '0123456789'
alph = 'abcdefgh'
alph_rus = 'абвгдеёжзийклмнопр'

print(id(alph_rus))

# for i in range(len(line)):
#     print(line[i])

for smb in alph_rus.upper():
    print(smb, ord(smb))
