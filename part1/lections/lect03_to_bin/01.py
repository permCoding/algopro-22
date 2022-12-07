def to_bin(dec, base=2):
    """ 
    для перевода дес числа   
    в СС с осн base
    """
    bin = ""    
    while dec > 0:
        mod, dec = dec % base, dec // base
        bin = bin + str(mod)
    return bin[::-1]  # reverse str


lst = [7, 8, 9, 10, 11, 127]
for elm in lst:
    print(f"{elm}\t{to_bin(elm)}")
