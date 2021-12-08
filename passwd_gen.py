from random import randint


def pwd_generator(symb_count=0):
    try:
        passwd = []
        while len(passwd) < symb_count:
            passwd.append(chr(randint(33, 127)))
        return ''.join(passwd)
    except TypeError:
        return 'wrong number'


if __name__ == '__main__':
    print(pwd_generator(8))

