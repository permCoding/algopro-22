from module import *


file_name = "csv/lang.csv"

lines = get_lines(file_name)
tuples = get_tuples(lines)

filtred = [tpl for tpl in tuples if tpl[3]]
# filtred = filter(lambda x: x[3], tuples)
for tpl in filtred:
    print(tpl)
