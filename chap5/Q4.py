""" The most simple but cheap solution """

def count_ones(i):
    count = 0
    while i > 0:
        if i&1 == 1:
            count += 1
        i >>= 1
    return count

def count_zeros(i):
    return 32 - count_ones(i)

def has_valid_next(i):
    if i == 0:
        return False
    
    count = 0
    while i&1 == 0:
        i >>= 1
        count += 1
    while i&1 == 1:
        i >>= 1
        count += 1

    if count == 31:
        return False
    
    return True

def has_valid_prev(i):
    while i&1 == 1:
        i >>= 1
    return True if i != 0 else False

def get_next_slow(i):
    if not has_valid_next(i):
        return -1

    num_ones = count_ones(i)
    i += 1
    while count_ones(i) != num_ones:
        i += 1
    return i

def get_prev_slow(i):
    if not has_valid_prev(i):
        return -1

    num_ones = count_ones(i)
    i -= 1
    while count_ones(i) != num_ones:
        i -= 1
    return i

if __name__ == '__main__':
    i = 13948
    p1 = get_prev_slow(i)
    n1 = get_next_slow(i)
    print(f'Previous : {p1} : {bin(p1)}')
    print(f'Target   : {i} : {bin(i)}')
    print(f'Next     : {n1} : {bin(n1)}')
