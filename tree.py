class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self._size = 1

    def _set_left(self, left):
        self.left = left
        if left is not None:
            left.parent = self

    def _set_right(self, right):
        self.right = right
        if right is not None:
            right.parent = self

    def insert_in_order(self, d):
        if d < self.data:
            if self.left is None:
                self._set_left(TreeNode(d))
            else:
                self.left.insert_in_order(d)
        else:
            if self.right is None:
                self._set_right(TreeNode(d))
            else:
                self.right.insert_in_order(d)
        self._size += 1

    def size(self):
        return self._size

    def isBST(self):
        if not self.left is None:
            if self.data < self.left.data or not self.left.isBST():
                return False

        if not self.right is None:
            if self.data >= self.right.data or not self.right.isBST:
                return False

        return True

    def height(self):
        left_height = self.left.height() if not self.left is None else 0
        right_height = self.right.height() if not self.right is None else 0
        return 1 + max(left_height, right_height)

    def find(self, d):
        if d == self.data:
            return self
        elif d <= self.data:
            return self.left.find(d) if self.left is not None else None
        elif d > self.data:
            return self.right.find(d) if self.right is not None else None
        else:
            return None

    @staticmethod
    def _create_minimal_BST(array, start, end):
        if end < start:
            return None
        mid = (start + end)//2
        n = TreeNode(array[mid])
        n._set_left(TreeNode._create_minimal_BST(array, start, mid-1))
        n._set_right(TreeNode._create_minimal_BST(array, mid+1, end))
        return n

    @staticmethod
    def create_minimal_BST(array):
        return TreeNode._create_minimal_BST(array, 0, len(array)-1)
