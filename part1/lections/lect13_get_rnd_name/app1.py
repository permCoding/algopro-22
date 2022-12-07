from generator import *


print(get_flat_list(10, 0, 100))

abits = get_objs_list(10, 160, 205)

for item in sorted(abits, key=lambda abit: abit[1], reverse=True)[:3]:
    print(item)
