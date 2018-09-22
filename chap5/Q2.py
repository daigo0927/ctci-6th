def print_binary(num):
    """
    Return binary representation of 0-1 real value
    
    Args:
    - float num: target value

    Returns:
    - str: binary representation of input value
    """
    if num >= 1 or num <= 0:
        return 'ERROR'

    binary = '.'
    while num > 0:
        if len(binary) > 32:
            return 'ERROR'
        r = num*2
        if r >= 1:
            binary += '1'
            num = r-1
        else:
            binary += '0'
            num = r
    return binary


def print_binary2(num):
    """
    Alternative solution
    """
    if num >= 1 or num <= 0:
        return 'ERROR'

    binary = '.'
    frac = 0.5
    while num > 0:
        # Setting a limit on length: 32 characters
        if len(binary) >= 32:
            return 'ERROR'
        
        if num >= frac:
            binary += '1'
            num -= frac
        else:
            binary += '0'
        frac /= 2
    return binary

if __name__ == '__main__':
    bs = print_binary(0.125)
    print(bs)

    for i in range(1000):
        num = i/1000.
        binary = print_binary(num)
        binary2 = print_binary2(num)
        if binary != 'ERROR' or binary2 != 'ERROR':
            print(f'{num} : {binary} {binary2}')
