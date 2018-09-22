import os, sys
sys.path.append(os.pardir)
import random
from utils.tree import TreeNode


class Tree:
    def __init__(self):
        self.root = None

    def size(self):
        return self.root.size() if self.root is not None else 0

    def get_random_node(self):
        if self.root is None:
            return None
        i = random.randint(0, self.size()-1)
        return self.root.get_ith_node(i)

    def insert_in_order(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.root.insert_in_order(value)
        

class TreeNode(TreeNode):
    def __init__(self, data):
        super().__init__(data)

    def get_ith_node(self, i):
        left_size = self.left.size() if self.left is not None else 0
        if i < left_size:
            return self.left.get_ith_node(i)
        elif i == left_size:
            return self
        else:
            return self.right.get_ith_node(i - (left_size+1))

    def insert_in_order(self, d):
        if d < self.data:
            if self.left is None:
                self.left = TreeNode(d)
            else:
                self.left.insert_in_order(d)
        else:
            if self.right is None:
                self.right = TreeNode(d)
            else:
                self.right.insert_in_order(d)
        self._size += 1

if __name__ == '__main__':
    counts = [0]*10
    for i in range(10**5):
        t = Tree()
        array = [1, 0, 6, 2, 3, 9, 4, 5, 8, 7]
        for x in array:
            t.insert_in_order(x)
        d = t.get_random_node().data
        counts[d] += 1
        
    for i in range(10):
        print(f'{i} : {counts[i]}')
