def bit_swap_required(a, b):
    count = 0
    if a > 0 and b < 0:
        b = abs(b)
        count += 1
    elif a < 0 and b > 0:
        a = abs(a)
        count += 1

    c = a^b
    while c != 0:
        count += 1
        c = c&(c-1)
    return count

if __name__ == '__main__':
    a = -23432
    b = 512132
    ans = bit_swap_required(a, b)
    print(f'{ans} bit required to convert {bin(a)} <-> {bin(b)}')
