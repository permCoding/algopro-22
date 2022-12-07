from generator import get_objs_list
from sorting import sort_select_tpl


lst = get_objs_list(20, 150, 210)
lst_s = sort_select_tpl(lst, pos=1, reverse=True)
for tpl in lst_s[:5]:
    tpls = list(map(str, tpl))
    print(f"{tpls[0].ljust(4, ' ')}{tpls[1].ljust(5, ' ')}{tpls[2]}")