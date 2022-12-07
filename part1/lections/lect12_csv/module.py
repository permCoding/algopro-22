def get_lines(file_name):
    with open(file_name) as f:
        lines = f.readlines()[1:]
        # ver 1
        # lines_new = []
        # for line in lines:
        #     lines_new.append(line.strip())
        # ver 2
        # lines_new = [line.strip() for line in lines]
        # ver 3
        lines_new = list(map(lambda line: line.strip(), lines))
    return lines_new


def get_tuples(lines):
    result = []
    for s in lines:
        lst = s.split(',')
        tpl = (int(lst[0]), lst[1], float(lst[2].strip('%')), bool(int(lst[3])))
        # result.append(tpl)
        result += [tpl]
    return result

