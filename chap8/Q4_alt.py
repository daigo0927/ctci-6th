def convert_int_to_set(x, set_):
    subset = []
    index = 0
    while x > 0:
        if x&1 == 1:
            subset.append(set_[index])
        index += 1
        x >>= 1
    return subset

def get_subsets(set_):
    all_subsets = []
    for k in range(1<<len(set_)):
        subset = convert_int_to_set(k, set_)
        all_subsets.append(subset)
    return all_subsets


if __name__ == '__main__':
    list_ = [1, 2, 3]
    print(f'Alls subsets of {list_} is')
    for subset in get_subsets(list_):
        print(subset)
