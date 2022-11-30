from module import *


file_in = "csv/lang.csv"
file_out = "csv/lang_.csv"

lines = get_lines(file_in)

with open(file_out, 'w', encoding='utf8') as f:
    for line in lines[:3]:
        f.write(line + '\n')
