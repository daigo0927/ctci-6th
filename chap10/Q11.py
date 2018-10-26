def sort_valley_peak(array):
    array = sorted(array)
    for i in range(1, len(array), 2):
        array = swap(array, i-1, i)
    return array
        
def swap(array, left, right):
    tmp = array[left]
    array[left] = array[right]
    array[right] = tmp
    return array

if __name__ == '__main__':
    array = [48, 40, 31, 62, 28, 21, 64, 40, 23, 17]
    print(f'original array : {array}')
    vp_array = sort_valley_peak(array)
    print(f'valley-peak array : {vp_array}')

