import matplotlib.pyplot as plt
import pandas as pd
import csv


# df = pd.read_csv('./frame_drivers.csv')
# df.cty

with open('./frame_drivers.csv','r') as f:
    reader = csv.reader(f)
    lst = [row for row in reader]

for e in lst: print(e[0], e[1])

"""
можно ли найти область Парето-оптимальных решений
два параметра
1)
- количество цилиндров - поменьше
- объём двигателя побольше
или наоборот:
2)
- количество цилиндров - побольше
- мощность двигателя поменьше
"""