def make_change(amount, denoms, index):
    if index >= len(denoms)-1:
        return 1
    denom_amount = denoms[index]
    ways = 0
    i = 0
    while i*denom_amount <= amount:
        amount_remain = amount - i*denom_amount
        ways += make_change(amount_remain, denoms, index+1)
        i += 1
    return ways

if __name__ == '__main__':
    denoms = [25, 10, 5, 1]
    amount = 100
    ways = make_change(amount, denoms, 0)
    print(f'{amount} cents can be change by {ways} patterns')
