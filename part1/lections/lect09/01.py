def get_lines(file_name, title=False):
    left = 1 if title else 0
    with open(file_name, mode="r", encoding='utf8') as f:
        lines = f.readlines()
        return list(map(lambda line: line.rstrip("\n"), lines))[left:]


lines = get_lines("./csv/abitura.csv", True)

sep = ','

print(lines[0].split(sep))
