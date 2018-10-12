def make_change(amount, denoms, index, map_):
    if map_[amount][index] > 0:
        return map_[amount][index]
    if index >= len(denoms)-1:
        return 1
    denom_amount = denoms[index]
    ways, i = 0, 0
    while i*denom_amount <= amount:
        amount_remain = amount - i*denom_amount
        ways += make_change(amount_remain, denoms, index+1, map_)
        i += 1
    map_[amount][index] = ways
    return ways

if __name__ == '__main__':
    denoms = [25, 10, 5, 1]
    amount = 100
    map_ = [[0]*len(denoms) for _ in range(amount+1)]
    ways = make_change(100, denoms, 0, map_)
    print(f'{amount} can be changed by {ways} patterns')
