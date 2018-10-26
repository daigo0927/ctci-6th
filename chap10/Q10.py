class RankNode:
    def __init__(self, d):
        self.data = d
        self.left_size = 0
        self.left = None
        self.right = None

    def insert(self, d):
        if d <= self.data:
            if self.left is not None:
                self.left.insert(d)
            else:
                self.left = RankNode(d)
            self.left_size += 1
        else:
            if self.right is not None:
                self.right.insert(d)
            else:
                self.right = RankNode(d)

    def get_rank(self, d):
        if d == self.data:
            return self.left_size
        elif d < self.data:
            if self.left is None:
                return -1
            else:
                return self.left.get_rank(d)
        else:
            right_rank = -1 if self.right is None else self.right.get_rank(d)
            if right_rank == -1:
                return -1
            else:
                return self.left_size+1+right_rank

def track(root, number):
    if root is None:
        root = RankNode(number)
    else:
        root.insert(number)
    return root

def get_rank_of_number(root, number):
    return root.get_rank(number)

if __name__ == '__main__':
    root = None
    numbers = [5, 1, 4, 4, 5, 9, 7, 13, 3]
    for n in numbers:
        root = track(root, n)

    for n in [1, 3, 4]:
        rank = get_rank_of_number(root, n)
        print(f'{n} is {rank}-rank at {numbers}')
