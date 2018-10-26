# This solution is a bit wring as the actual setting
def find_dupricate_number(numbers):
    bit_field = [0]*(32000//8)

    dups = set([])
    for n in numbers:
        if bit_field[(n-1)//8] & 1<<((n-1)%8):
            dups.add(n)
        else:
            bit_field[(n-1)//8] |= 1<<((n-1)%8)

    dups_ = [dups.pop() for _ in range(5)]
    print(f'{dups_} ... are opened')

if __name__ == '__main__':
    import numpy as np
    # numbers does not nucessarily have whole number between 0-32000
    numbers = np.random.random_integers(1, 32000, 40000)
    find_dupricate_number(numbers)
