def longest_seq(n):
    """
    Get the length of the longest 1s sequence

    Args: int n: input number
    Returns: int: length of the longest sequence
    """
    if n == -1:
        raise ValueError('Invalid argument for n : {n}')
    seqs = get_alternating_seqs(n)
    return find_longest_seq(seqs)

def get_alternating_seqs(n):
    """
    Get alternating sequences by flipping 0 and 1
    
    Args: int n: input number
    Returns: list<int>: list of length of 1s or 0s sequences
    """
    seqs = []

    searching_for = 0
    counter = 0
    for i in range(len(bin(n))-2):
        if (n&1) != searching_for:
            seqs.append(counter)
            searching_for = n&1
            counter = 0
            
        counter += 1
        n >>= 1
    seqs.append(counter)

    return seqs

def find_longest_seq(seq):
    """
    Find the longest sequence allowing 0-1 flip

    Args: list<int> seq: target sequences
    Returns: int: length of the longest sequence
    """
    max_seq = 1
    for i in range(0, len(seq), 2):
        zeros_seq = seq[i]
        ones_seq_left = seq[i-1] if i-1 >= 0 else 0
        ones_seq_right = seq[i+1] if i+1 < len(seq) else 0

        this_seq = 0
        if zeros_seq == 1: # Can merge
            this_seq = ones_seq_left + 1 + ones_seq_right
        elif zeros_seq > 1: # Just add a zero to either side
            this_seq = 1+max(ones_seq_right, ones_seq_left)
        elif zeros_seq == 0: # No zero, but take either side
            this_seq = max(ones_seq_right, ones_seq_left)

        max_seq = max(this_seq, max_seq)
    return max_seq

if __name__ == '__main__':
    num = 1775
    ans = longest_seq(num)
    print(f'{num} -> {ans}')
                    
