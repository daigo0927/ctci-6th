BYTES = 4

def flip_bit(a):
    if a&(a+1) == 0:
        return len(bin(a))-2

    cur_length = 0
    prev_length = 0
    max_length = 0
    while a != 0:
        if a&1 == 1:
            cur_length += 1
        elif a&1 == 0:
            prev_length = 0 if a&2 == 0 else cur_length
            cur_length = 0

        max_length = max(prev_length+cur_length+1, max_length)
        a >>= 1
        
    return max_length

if __name__ == '__main__':
    cases = [(0, 1), (1, 1), (15, 4), (1775, 8)]
    for num, ans in cases:
        x = flip_bit(num)
        result = 'valid' if x == ans else 'invalid'
        print(f'Case1 {num} -> {x}: {result}')
