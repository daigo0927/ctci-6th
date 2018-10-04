def min_product(a, b):
    bigger = b if a < b else a
    smaller = a if a < b else b
    return min_product_helper(smaller, bigger)

def min_product_helper(smaller, bigger):
    global counter
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger

    s = smaller>>1
    side1 = min_product_helper(s, bigger)
    side2 = side1
    if smaller%2 == 1:
        counter += 1
        side2 = min_product_helper(smaller-s, bigger)

    counter += 1
    return side1 + side2

if __name__ == '__main__':
    counter = 0
    a, b = 13494, 22323
    product = a*b
    min_prod = min_product(a, b)
    print(f'Calculate result {product == min_prod} with {counter}.')
