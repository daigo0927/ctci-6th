def count_ways(n):
    '''
    Count the number of paths by recursive operation
    Args: int n: # of stairs
    Returns: int: patterns of path
    '''
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)
    
if __name__ == '__main__':
    n = 20
    ways = count_ways(n)
    print(f'{ways} ways found.')
