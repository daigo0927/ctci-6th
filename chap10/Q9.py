def find_element(matrix, elem):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == elem:
            return True
        elif matrix[row][col] > elem:
            col -= 1
        else:
            row += 1

    return False

if __name__ == '__main__':
    matrix = [[15, 20, 40, 85],
              [20, 35, 80, 95],
              [30, 55, 95, 105],
              [40, 80, 100, 120]]
    elem = 55
    if find_element(matrix, elem):
        print('True')
    else:
        print('False')
