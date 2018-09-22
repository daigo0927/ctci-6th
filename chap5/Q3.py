SEQ_LENGTH = 32

def get_bit(num, i):
    """
    Return if i-th digit of given number is 1:True or 0:False

    Args:
    - int num: given number
    - int i: target digit

    Returns:
    - bool: if i-th digits is 1 or 0
    """
    return (num&(1<<i)) != 0

def longest_seq(n):
    """
    Get longest 1s sequence of input value with flip each bit
    
    Args:
    - int n: input value

    Return:
    - int: maximum length of 1s sequences
    """
    max_seq = 0
    for i in range(SEQ_LENGTH):
        max_seq = max(max_seq, longest_seq_of_1s(n, i))

    return max_seq

def longest_seq_of_1s(n, index_to_ignore):
    """
    Get longest length of 1s sequences

    Args:
    - int n: input value
    - int index_to_ignore: flipped (= ignored) index

    Returns:
    - int: length of longest 1s sequence
    """
    max_ = 0
    counter = 0
    for i in range(SEQ_LENGTH):
        if i == index_to_ignore or get_bit(n, i):
            counter += 1
            max_ = max(counter, max_)
        else:
            counter = 0
    return max_

if __name__ == '__main__':
    num = 1775
    ans = longest_seq(num)
    print(f'{num} -> {ans}')
