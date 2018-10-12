GRID_SIZE = 8

def place_queens(row, cols, results):
    if row == GRID_SIZE:
        # results.append(cols)
        return 1
    else:
        ways = 0
        for col in range(GRID_SIZE):
            if check_valid(cols, row, col):
                cols[row] = col
                # results = place_queens(row+1, cols, results)
                ways += place_queens(row+1, cols, results)
        return ways
                

def check_valid(cols, row1, col1):
    for row2 in range(row1):
        col2 = cols[row2]

        if col1 == col2:
            return False

        col_dist = abs(col2 - col1)
        row_dist = row1 - row2
        if col_dist == row_dist:
            return False
        
    return True

if __name__ == '__main__':
    results = []
    cols = [-1]*GRID_SIZE
    ways = place_queens(0, cols, results)
    print(f'8x8 board has {ways} patterns of queen placements')
