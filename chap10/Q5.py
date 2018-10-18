def search(strings, string, first, last):
    if strings is None or string is None or string == '':
        return -1
    if first > last:
        return -1

    mid = (last + first)//2
    if strings[mid] == '':
        left = mid-1
        right = mid+1
        while True:
            if left < first and right > last:
                return -1
            elif right <= last and strings[right] != '':
                mid = right
                break
            elif left >= first and strings[left] != '':
                mid = left
                break

            right += 1
            left += 1

    if string == strings[mid]:
        return mid
    elif strings[mid] < string:
        return search(strings, string, mid+1, last)
    else:
        return search(strings, string, first, mid-1)

if __name__ == '__main__':
    strings = ['apple', '', '', 'banana', '', '', '', 'carrot',
               'duck', '', '', 'eel', '', 'flower']
    for string in strings:
        print(f"{string} is at {search(strings, string, 0, len(strings)-1)}")
