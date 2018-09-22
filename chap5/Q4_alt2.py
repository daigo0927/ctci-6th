""" An arithmetic solution """

def get_next_arith(n):
    c = n
    c0 = 0
    c1 = 0
    while c&1 == 0 and c != 0:
        c0 += 1
        c >>= 1

    while c&1 == 1:
        c1 += 1
        c >>= 1

    if c0+c1 == 31 or c0+c1 == 0:
        return -1

    # Arithmetically,
    # 2^c0 = 1 << c0
    # 2^(c1-1) = 1 << (c0 - 1)
    # next = n + 2^c0 + 2^(c1-1) - 1
    return n + (1<<c0) + (1<<(c1-1)) - 1

def get_prev_arith(n):
    tmp = n
    c0 = 0
    c1 = 0
    while tmp&1 == 1 and tmp != 0:
        c1 += 1
        tmp >>= 1

    if tmp == 0:
        return -1

    while tmp&1 == 0 and tmp != 0:
        c0 += 1
        tmp >>= 1

    # Arithmetically,
    # 2^c1 = 1 << c1
    # 2^(c0 - 1) = 1 << (c0 - 1)
    return n - (1<<c1) - (1<<(c0-1)) + 1


if __name__ == '__main__':
    i = 13948
    p1 = get_prev_arith(i)
    n1 = get_next_arith(i)
    print(f'Previous : {p1} : {bin(p1)}')
    print(f'Target   : {i} : {bin(i)}')
    print(f'Next     : {n1} : {bin(n1)}')
