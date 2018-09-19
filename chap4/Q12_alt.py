import os, sys
sys.path.append(os.pardir)
from tree import TreeNode

def count_paths_with_sum(node, sum_tar, sum_run = 0, count_paths = dict()):
    """
    Args:
    - TreeNode node: node of a tree
    - int sum_tar: sum of the target path
    - int sum_run: sum of the running range
    - dictionary<int, int> count_paths: map from paths sum to count

    Returns:
    - int: 
    """
    if node is None:
        return 0

    sum_run += node.data

    # Count paths with sum ending at the current node
    sum_ = sum_run - sum_tar
    paths_total = count_paths.get(sum_, 0)

    # If sum_run equals sum_tar, one additional path starts at root. Add in this path
    if sum_run == sum_tar:
        paths_total += 1

    # Add sum_run to count_paths
    count_paths = increment_hashtable(count_paths, sum_run, 1)

    # Count paths with sum on the left and right
    paths_total += count_paths_with_sum(node.left, sum_tar, sum_run, count_paths)
    paths_total += count_paths_with_sum(node.right, sum_tar, sum_run, count_paths)

    count_paths = increment_hashtable(count_paths, sum_run, -1)
    return paths_total

def increment_hashtable(hashtable, key, delta):
    """
    Increment the hash value specified by the given key

    Args:
    - dictionary<int, int> hashtable
    - int key: hashkey
    - int delta: increment value

    Returns:
    - dictionary<int, int>: incremented hashtable
    """
    count_new = hashtable.get(key, 0) + delta
    if count_new == 0 and key in hashtable.keys():
        # Remove if the value equals 0 to redume space usage
        hashtable.pop(key)
    else:
        hashtable[key] = count_new
        
    return hashtable


if __name__ == '__main__':
    # Tree1
    root1 = TreeNode(5);
    root1.left = TreeNode(3)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(-8)
    root1.left.right = TreeNode(8)
    root1.right.left = TreeNode(2)
    root1.right.right = TreeNode(6)
    ans1 = count_paths_with_sum(root1, 0)
    print(f'Tree1 contains {ans1} of with {0} summation')

    # Tree2
    root2 = TreeNode(-7)
    root2.left = TreeNode(-7)
    root2.left.right = TreeNode(1)
    root2.left.right.left = TreeNode(2)
    root2.right = TreeNode(7)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(20)
    root2.right.right.left = TreeNode(0)
    root2.right.right.left.left = TreeNode(-3)
    root2.right.right.left.left.right = TreeNode(2)
    root2.right.right.left.left.right.left = TreeNode(1)
    ans2 = count_paths_with_sum(root2, -14)
    print(f'Tree2 contains {ans2} of with {-14} summation')

    # Tree3
    root3 = TreeNode(0)
    root3.left = TreeNode(0)
    root3.right = TreeNode(0)
    root3.right.left = TreeNode(0)
    root3.right.left.right = TreeNode(0)
    root3.right.right = TreeNode(0)
    ans3 = count_paths_with_sum(root3, 0)
    ans4 = count_paths_with_sum(root3, 4)
    print(f'Tree3 contains {ans3} of with {0} summation')
    print(f'Tree3 contains {ans4} of with {4} summation')
