from collections import deque
from tree import TreeNode

def create_tree_from_array(array):
    """
    Create tree by mapping the array left to right, top to bottom
    
    Args:
    - list array: list of contents values

    Returns:
    - TreeNode root: root node
    """
    if len(array) > 0:
        root = TreeNode(array[0])
        que = deque()
        que.append(root)
        done = False
        i = 1
        while not done:
            r = que[0]
            if r.left is None:
                r.left = TreeNode(array[i])
                i += 1
                que.append(r.left)
            elif r.right is None:
                r.right = TreeNode(array[i])
                i += 1
                que.append(r.right)
            else:
                _ = que.popleft()
                
            if i == len(array):
                done = True

        return root
    else:
        return None
