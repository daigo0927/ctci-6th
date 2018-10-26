# This solution is a bit wring as the actual setting
def find_open_number(numbers):
    bit_field = [0]*(2**16//8)
    for n in numbers:
        bit_field[n//8] |= 1<<(n%8)

    opens = []
    for i in range(len(bit_field)):
        for j in range(8):
            if bit_field[i] & (1<<j) == 0:
                opens.append(i*8+j)

    print(f'{opens[:5]} ... are opened')

if __name__ == '__main__':
    import numpy as np
    numbers = np.random.random_integers(0, 2**15, 2**16)
    find_open_number(numbers)
