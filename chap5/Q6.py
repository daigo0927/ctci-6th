def bit_swap_required(a, b):
    count = 0
    c = a^b
    while not c in [0, -1]:
        count += c&1
        c >>= 1
    return count

if __name__ == '__main__':
    a = -23432
    b = 512132
    ans = bit_swap_required(a, b)
    print(f'{ans} bit required to convert {bin(a)} <-> {bin(b)}')
