from random import choice


def _get_symbol():
    """получить один случайный символ"""
    alph = ''.join([chr(i) for i in range(65, 65+26)])
    alph += alph.lower()
    return choice(alph)


def get_password(len_pswd=8):
    """получить пароль длинной len_pswd символов"""
    pswd = ""
    for i in range(len_pswd):
        pswd += _get_symbol()
    return pswd


if __name__ == "__main__":
    new_pswd = get_password()
    print(new_pswd)