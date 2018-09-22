def update_bits(n, m, i, j):
    """
    Update given bits n by inserting m with j-i range
    
    Args:
    - int n: target value 1 to be inserted
    - int m: target value 2 to insert
    - int i, j: right and left locations of insertion

    Return:
    - int: updated (inserted) value
    """
    # Problem regularization
    if i >= 32 or j < i:
        return 0

    # Create a mask to clear bits i through j in n
    # EXAMPLE: i = 2, j = 4, reesult should be 11100011.
    all_ones = (1<<32)-1

    left = all_ones<<(j+1) # 1s through position j, then 0s, left = 11100000
    right = (1<<i)-1 # 1's after position i, right = 00000011
    mask = left|right # All 1s, except for 0s between i and j, mask = 11100011

    # Clear i through j, then put m in there
    n_cleared = n&mask # Clear bits j through i.
    m_shifted = m<<i # Move m into correct position

    # Get bit-or, and we're done!
    return n_cleared | m_shifted

if __name__ == '__main__':
    a = 103217
    print(f'a : {bin(a)}')
    b = 13
    print(f'b : {bin(b)}')
    c = update_bits(a, b, 4, 12)
    print(f'c : {bin(c)}')
