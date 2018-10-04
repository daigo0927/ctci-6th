def get_path(maze):
    '''
    Get available # of paths
    Args: int[][] maze: maze 2-dim list
    Returns: int: # of paths
    '''
    if maze is None or len(maze) == 0:
        return None
    path = []
    if is_path(maze, len(maze)-1, len(maze[0])-1, path):
        return path
    return None

def is_path(maze, row, col, path):
    if col < 0 or row < 0 or not maze[row][col]:
        return False

    at_origin = (row == 0) and (col == 0)

    if at_origin or is_path(maze, row, col-1, path) or is_path(maze, row-1, col, path):
        point = (row, col)
        path.append(point)
        return True
    return False


if __name__ == '__main__':
    row, col = 3, 4
    maze = [[True]*col for _ in range(row)]
    forbid_y, forbid_x = 1, 2
    maze[forbid_y][forbid_x] = False
    print(get_path(maze))
