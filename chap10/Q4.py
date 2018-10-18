# Unable to use len(array)
class Listy:
    def __init__(self, array):
        self.array = array

    def __len__(self):
        raise NotImplementedError('len(listy) is not implemented')

    def element_at(self, index):
        # only internally able to get size
        if index >= len(self.array):
            return -1
        else:
            return self.array[index]

def binary_search(listy, value, low, high):
    while low <= high:
        mid = (low+high)//2
        middle = listy.element_at(mid)
        if middle > value or middle == -1:
            high = mid-1
        elif middle < value:
            low = mid+1
        else:
            return mid

    return -1

def search(listy, value):
    index = 1
    while listy.element_at(index) != -1 and listy.element_at(index) < value:
        index *= 2
    return binary_search(listy, value, index//2, index)

if __name__ == '__main__':
    array = [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18]
    listy = Listy(array)
    for a in array:
        print(f'{a} is at {search(listy, a)}')
    print(f'{15} is at {search(listy, 15)}')
