def sort_valley_peak(array):
    for i in range(1, len(array), 2):
        biggest_index = max_index(array, i-1, i, i+1)
        if i != biggest_index:
            array = swap(array, i, biggest_index)
    return array
        
def swap(array, left, right):
    tmp = array[left]
    array[left] = array[right]
    array[right] = tmp
    return array

def max_index(array, a, b, c):
    l = len(array)
    a_value = array[a] if a >= 0 and a < l else -float('inf')
    b_value = array[b] if b >= 0 and b < l else -float('inf')
    c_value = array[c] if c >= 0 and c < l else -float('inf')

    max_value = max(a_value, b_value, c_value)

    if a_value == max_value:
        return a
    elif b_value == max_value:
        return b
    else:
        return c

if __name__ == '__main__':
    array = [48, 40, 31, 62, 28, 21, 64, 40, 23, 17]
    print(f'original array : {array}')
    vp_array = sort_valley_peak(array)
    print(f'valley-peak array : {vp_array}')











