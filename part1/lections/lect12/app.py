from module import *


file_name = "csv/lang.csv"

lines = get_lines(file_name)
tuples = get_tuples(lines)

tuples.sort(key=lambda x: x[1])
for tpl in tuples:
    print(f"{tpl[1].ljust(12, ' ')}{tpl[2]}%")

# sorted = sorted(tuples, key=lambda elm: elm[2], reverse=True)
# for tpl in sorted:
#     # print(tpl[1].ljust(12, ' '), tpl[2], '%', sep='')
#     print(f"{tpl[1].ljust(12, ' ')}{tpl[2]}%")
