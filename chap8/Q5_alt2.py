def min_product(a, b):
    bigger = b if a < b else a
    smaller = a if a < b else b
    return min_product_helper(smaller, bigger)

def min_product_helper(smaller, bigger):
    global counter
    if smaller == 0: return 0
    elif smaller == 1: return bigger
    
    s = smaller>>1
    half_prod = min_product_helper(s, bigger)

    if smaller%2 == 0:
        counter += 1
        return half_prod + half_prod
    else:
        counter += 2
        return half_prod + half_prod + bigger


if __name__ == '__main__':
    counter = 0
    a, b = 13494, 22323
    product = a*b
    min_prod = min_product(a, b)
    print(f'Calculate result {min_prod}({product == min_prod}) with {counter}.')
