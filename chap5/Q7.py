def swap_odd_even_bits(x):
    return ((x & 0xaaaaaaaa) >> 1) | ((x & 0x55555555) << 1)

if __name__ == '__main__':
    a = 234321
    b = swap_odd_even_bits(a)
    print(f'Original : {bin(a)}')
    print(f'Swapped  : {bin(b)}')
    
