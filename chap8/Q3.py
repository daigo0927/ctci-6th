import random

def magic_slow(array):
    '''
    Get magic index (slow)
    Args: list<int> array: target sorted array
    Returns: int: magic index, -1 if not exists
    '''
    for i in range(len(array)):
        if array[i] == i:
            return i
    return -1

def magic_fast(array, start, end):
    if end < start:
        return -1

    mid = (start + end)//2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return magic_fast(array, start, mid-1)
    else:
        return magic_fast(array, mid+1, end)
    

if __name__ == '__main__':
    array = [-14, -12, 0, 1, 2, 5, 9, 10, 23, 25, 30]
    print(f'{magic_slow(array)} is the magic index in {array} (slow ver.)')
    print(f'{magic_fast(array, 0, len(array)-1)} is the magic index in {array} (fast ver.)')
