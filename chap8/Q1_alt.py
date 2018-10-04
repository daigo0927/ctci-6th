def count_ways(n):
    '''
    Count ways of upstairs
    Args: int n: # of upstairs
    Returns: int: ways
    '''
    map_ = [-1]*(n+1)
    return count_ways_(n, map_)
    
def count_ways_(n, memo):
    '''
    Memorize and calculate ways
    Args:
    - int n: # of current stair
    - int[] memo: memo of observed result
    Returns: int: sum of ways
    '''
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = count_ways_(n-1, memo) + count_ways_(n-2, memo) + count_ways_(n-3, memo)
        return memo[n]

if __name__ == '__main__':
    n = 20
    ways = count_ways(n)
    print(f'{ways} ways found.')
