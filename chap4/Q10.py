import os, sys
sys.path.append(os.pardir)
import utils

def contains_tree(tree1, tree2):
    """
    Validate if tree1 contains tree2
    """
    string1 = get_order_string(tree1, '')
    string2 = get_order_string(tree2, '')
    print(string1, string2)
    
    return True if string2 in string1 else False

def get_order_string(node, string):
    if node is None:
        string += "x"
        return string

    string += str(node.data)
    string = get_order_string(node.left, string)
    string = get_order_string(node.right, string)
    return string

if __name__ == '__main__':
    # True case
    array1 = [1, 2, 1, 3, 1, 1, 5]
    array2 = [2, 3, 1]
    
    tree1 = utils.create_tree_from_array(array1)
    tree2 = utils.create_tree_from_array(array2)

    if contains_tree(tree1, tree2):
        print('tree2 is a subtree of tree1')
    else:
        print('tree2 is not a subtree of tree1')

    array3 = [1, 2, 3]
    tree3 = utils.create_tree_from_array(array3)
    if contains_tree(tree1, tree3):
        print('tree3 is a subtree of tree1')
    else:
        print('tree3 is not a subtree of tree1')
    
