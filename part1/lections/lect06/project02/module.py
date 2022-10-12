def palindrom(line, fail_symbols="!-.' ?\""):
    for smb in fail_symbols:
        line = line.replace(smb, '')
    return line.lower() == line[::-1].lower()
