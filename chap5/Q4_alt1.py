def get_next(n):
    c = n
    c0 = 0
    c1 = 0
    while c&1 == 0 and c != 0:
        c0 += 1
        c >>= 1

    while c&1 == 1:
        c1 += 1
        c >>= 1

    # If c is 0, then n is a sequence of 1s followed by a sequence of 0s.
    # This is already the biggest number with c1 ones. Return error
    if c0+c1 == 31 or c0+c1 == 0:
        return -1

    # Position of right-most non-trailing 0 (where the right most bit is bit 0)
    pos = c0+c1

    # Flip the right-most non-trailing 0 (which will be at position pos)
    n |= (1<<pos)

    # Clear all bits to the right of pos
    n &= ~((1<<pos) - 1)

    # Put (ones-1) 1s on the right
    n |= (1 << (c1-1)) - 1

    return n

def get_prev(n):
    tmp = n
    c0 = 0
    c1 = 0
    while tmp&1 == 1:
        c1 += 1
        tmp >>= 1

    # If tmp is 0, then the number is a sequence of 0s folowed by a sequence of 1s,
    # This is already the smallest number with c1 ones. Return -1 for an error
    if tmp == 0:
        return -1

    while tmp&1 == 0 and tmp != 0:
        c0 += 1
        tmp >>= 1

    # Position od right-most non-trailing one (where the right most bit is bit 0)
    p = c0+c1

    # Flip right-most non-trailing one.
    # Clears from bit p onwards (to the right)
    n &= ((~0) << (p+1))

    # Create a sequence of (c1+1) 1s.
    # Sequence of (c1+1) ones
    mask = (1<<(c1+1))- 1

    # Move the ones to be right up next to bit p
    n |= mask << (c0-1)

    return n
    

if __name__ == '__main__':
    i = 13948
    p1 = get_prev(i)
    n1 = get_next(i)
    print(f'Previous : {p1} : {bin(p1)}')
    print(f'Target   : {i} : {bin(i)}')
    print(f'Next     : {n1} : {bin(n1)}')
