SEQ_LENGTH = 32

def get_max_seq(seqs):
    """
    Get length of the longest sequences of 1s by flipping

    Args: list<int> seqs: three sequences ordered as (0s, then 1s, then 0s)
    Returns: int: length of the longest sequence
    """
    if seqs[1] == 1: # single 0 -> marge sequences
        return seqs[0] + seqs[2] + 1
    elif seqs[1] == 0: # no-0s -> take one side
        return max(seqs[0], seqs[2])
    else: # manu 0s -> take side, add 1 (flip a bit)
        return max(seqs[0], seqs[2]) + 1

def shift(seqs):
    """ Shift the given list """
    seqs[2] = seqs[1]
    seqs[1] = seqs[0]
    seqs[0] = 0
    return seqs

def longest_seq(n):
    """
    Get the longest sequence

    Args: int n: target number
    Returns: int, length of the longest 1s sequence
    """
    searching_for = 0
    seqs = [0, 0, 0]
    max_seq = 1

    for i in range(SEQ_LENGTH):
        if (n&1) != searching_for:
            if searching_for == 1: # End of 1s+0s+1s sequence
                max_seq = max(max_seq, get_max_seq(seqs))

            searching_for = n&1 # Flip 1->0 or 0->1
            seqs = shift(seqs) # Shift sequences
            
        seqs[0] += 1
        n >>= 1

    if searching_for == 0: # Check final set f sequences
        seqs = shift(seqs)
        final_seq = get_max_seq(seqs)
        
    return max_seq

if __name__ == '__main__':
    num = 1775
    ans = longest_seq(num)
    print(f'{num} -> {ans}')
