def get_subsets(set_, index):
    '''
    Get subset of given set
    Args:
    - list<int> set_: target set
    - int index: index
    Returns: list<list<int>>: all subsets
    '''
    if len(set_) == index:
        all_subsets = [[]]
    else:
        all_subsets = get_subsets(set_, index+1)
        item = set_[index]
        more_subsets = []
        for subset in all_subsets:
            new_subset = subset + [item]
            more_subsets.append(new_subset)
            
        all_subsets += more_subsets

    return all_subsets

if __name__ == '__main__':
    list_ = [1, 2, 3]
    print(f'Alls subsets of {list_} is')
    for subset in get_subsets(list_, 0):
        print(subset)
