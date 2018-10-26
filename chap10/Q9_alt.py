class Coordinate:
    def __init__(self, r, c):
        self.row = r
        self.col = c

    def inbounds(self, matrix):
        return self.row >= 0 and self.col >= 0\
            and self.row < len(matrix) and self.col < len(matrix[0])

    def is_before(self, p):
        return self.row <= p.row and self.col <= p.col

    def clone(self):
        return Coordinate(self.row, self.col)

    def move_down_right(self):
        self.row += 1
        self.col += 1

    def set_to_average(self, cood_min, cood_max):
        self.row = (cood_min.row + cood_max.row)//2
        self.col = (cood_min.col + cood_max.col)//2


def partition_and_search(matrix, origin, dest, pivot, x):
    lower_left_origin = Coordinate(pivot.row, origin.col)
    lower_left_dest = Coordinate(dest.row, pivot.col-1)
    upper_right_origin = Coordinate(origin.row, pivot.col)
    upper_right_dest = Coordinate(pivot.row-1, dest.col)

    lower_left = find_element(matrix, lower_left_origin, lower_left_dest, x)
    if lower_left is None:
        return find_element(matrix, upper_right_origin, upper_right_dest, x)
    return lower_left

        
def find_element(matrix, origin, dest, x):
    if not origin.inbounds(matrix) or not dest.inbounds(matrix):
        return None
    if matrix[origin.row][origin.col] == x:
        return origin
    elif not origin.is_before(dest):
        return None

    # Set start to start of diagonal and end to the end of the diagonal
    # Since the grid may not be square, the end of the diagonal may not equal dest.
    start = origin.clone()
    diag_dist = min(dest.row-origin.row, dest.col-origin.col)
    end = Coordinate(start.row+diag_dist, dest.col-origin.col)
    p = Coordinate(0, 0)
    
    # Do binary search on the diagonal, looking for the dirst element greater than x
    while start.is_before(end):
        p.set_to_average(start, end)
        if x > matrix[p.row][p.col]:
            start.row = p.row+1
            start.col = p.col+1
        else:
            end.row = p.row-1
            end.col = p.col-1

    return partition_and_search(matrix, origin, dest, start, x)

if __name__ == '__main__':
    matrix = [[15, 30,  50,  70,  73],
              [35, 40, 100, 102, 120],
              [36, 42, 105, 110, 125],
              [46, 51, 106, 111, 130],
              [48, 55, 109, 140, 150]]
    elem = 111

    cood_origin = Coordinate(0, 0)
    cood_dest = Coordinate(4, 4)
    c = find_element(matrix, cood_origin, cood_dest, elem)
    if c is not None:
        print(f'{elem} is at row:{c.row}, col:{c.col} of below')
        for m in matrix:
            print(m)
    else:
        print(f'{elem} cound not be found')
