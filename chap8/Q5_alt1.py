def min_product(a, b):
    bigger = b if a < b else a
    smaller = a if a < b else b
    memo = [-1]*(smaller+1)

    return min_prod(smaller, bigger, memo)

def min_prod(smaller, bigger, memo):
    global counter
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    elif memo[smaller] > 0:
        return memo[smaller]

    s = smaller>>1
    side1 = min_prod(s, bigger, memo)
    side2 = side1
    if smaller%2 == 1:
        counter += 1
        side2 = min_prod(smaller-s, bigger, memo)

    # Sum and cash
    counter += 1
    memo[smaller] = side1 + side2
    return memo[smaller]
    

if __name__ == '__main__':
    counter = 0
    a, b = 13494, 22323
    product = a*b
    min_prod = min_product(a, b)
    print(f'Calculate result {min_prod}({product == min_prod}) with {counter}.')
