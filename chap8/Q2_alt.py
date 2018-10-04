def get_path_memorized(maze):
    '''
    Get path by memolization
    Args: bool[][] maze: target maze by 2D list
    Returns: list<tuple(int*2)> path
    '''
    if maze == None or len(maze) == 0:
        return None
    path = []
    failed_points = []
    if is_path_memorized(maze, len(maze)-1, len(maze[0])-1, path, failed_points):
        return path
    return None

def is_path_memorized(maze, row, col, path, failed_points):
    if col < 0 or row < 0 or not maze[row][col]:
        return False
    point = (row, col)

    if point in failed_points:
        return False

    at_origin = (row == 0) and (col == 0)

    if at_origin or is_path_memorized(maze, row-1, col, path, failed_points) \
       or is_path_memorized(maze, row, col-1, path, failed_points):
        path.append(point)
        return True

    failed_points.append(point)
    return False


if __name__ == '__main__':
    row, col = 3, 4
    maze = [[True]*col for _ in range(row)]
    forbid_y, forbid_x = 1, 2
    maze[forbid_y][forbid_x] = False
    print(get_path_memorized(maze))
