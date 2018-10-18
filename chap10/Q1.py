def merge(a, b, lastA, lastB):
    index_merged = lastB + lastA - 1
    indexA = lastA - 1
    indexB = lastB - 1

    while indexB >= 0:
        if indexA >= 0 and a[indexA] > b[indexB]:
            a[index_merged] = a[indexA]
            indexA -= 1
        else:
            a[index_merged] = b[indexB]
            indexB -= 1
        index_merged -= 1

    return a

if __name__ == '__main__':
    a = [2, 3, 4, 5, 6, 8, 10, 100, 0, 0, 0, 0, 0, 0]
    b = [1, 4, 7, 6, 7, 7]
    merged = merge(a, b, 8, 6)
    print(merged)
