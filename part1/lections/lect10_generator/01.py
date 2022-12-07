def get(line):
    i = 0
    while i < len(line):
        print(line[i])
        i += 1


def replace_ind(line, ind, smb_out):
    return line[:ind] + smb_out + line[ind+1:]


def replace_all(line, smb_in, smb_out):
    line_new = ""
    for smb in line:
        if smb == smb_in:
            smb = smb_out
        line_new += smb
    return line_new


line = "a awmb a vfg a ds a xaaa"
# get(line)

smb_in, smb_out = 'a', 'p'
ind = line.find(smb_in)
line = replace_ind(line, ind, smb_out)
print(line)

print(replace_all(line, smb_in, smb_out))
