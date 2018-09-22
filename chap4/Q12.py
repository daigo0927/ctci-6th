import os, sys
sys.path.append(os.pardir)
from utils.tree import TreeNode

def count_paths_with_sum(root, sum_tar):
    """
    Args:
    - TreeNode root
    - int sum_tar

    Returns:
    - int sum of paths
    """
    if root is None:
        return 0

    # Count pats with sum starting from the root node
    paths_from_root = count_paths_with_sum_from_node(root, sum_tar, 0)
    # Try the nodes on the left and right
    paths_on_left = count_paths_with_sum(root.left, sum_tar)
    paths_on_right = count_paths_with_sum(root.right, sum_tar)

    return paths_from_root + paths_on_left + paths_on_right

def count_paths_with_sum_from_node(node, sum_tar, sum_cur):
    """
    Args:
    - TreeNode node : starting node
    - int sum_tar : target sum
    - int sum_cur : current sum

    Returns
    - int paths_total : sum of total paths
    """
    if node is None:
        return 0

    sum_cur += node.data

    paths_total = 0
    if sum_cur == sum_tar:
        paths_total += 1

    paths_total += count_paths_with_sum_from_node(node.left, sum_tar, sum_cur)
    paths_total += count_paths_with_sum_from_node(node.right, sum_tar, sum_cur)

    return paths_total


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
