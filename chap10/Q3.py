def search(a, x):
    return _search(a, 0, len(a)-1, x)

def _search(a, left, right, x):
    mid = (left + right)//2
    if x == a[mid]:
        return mid
    if right < left:
        return -1


    # Operation for inflection point caused by rotation
    if a[left] < a[mid]:
        if x >= a[left] and x < a[mid]:
            return _search(a, left, mid-1, x)
        else:
            return _search(a, mid+1, right, x)
    elif a[mid] < a[left]:
        if x > a[mid] and x <= a[right]:
            return _search(a, mid+1, right, x)
        else:
            return _search(a, left, mid-1, x)
    elif a[left] == a[mid]:
        if a[mid] != a[right]:
            return _search(a, mid+1, right, x)
        else:
            result = _search(a, left, mid-1, x)
            if result == -1:
                return _search(a, mid+1, right, x)
            else:
                return result
    
    return -1

if __name__ == '__main__':
    a = [2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2]
    for n in [2, 3, 4, 1, 8]:
        print(f'{n} is at {search(a, n)}')
