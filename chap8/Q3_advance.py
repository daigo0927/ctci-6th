def magic_fast(array, start, end):
    if end < start:
        return -1

    mid_index = (start + end)//2
    mid_value = array[mid_index]
    if mid_value == mid_index:
        return mid_index

    # Search left
    left_index = min(mid_index-1, mid_value)
    left = magic_fast(array, start, left_index)
    if left >= 0:
        return left

    # Search right
    right_index = max(mid_index+1, mid_value)
    right = magic_fast(array, right_index, end)
    return right

if __name__ == '__main__':
    array = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
    print(f'{magic_fast(array, 0, len(array))} is the magix index in {array}')
