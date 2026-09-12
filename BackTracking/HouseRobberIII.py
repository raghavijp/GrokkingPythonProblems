from TreeNode import *
from BinaryTree import *


def heist(root):
    if root == None:
        return [0,0]

    left_subtree = heist(root.left)
    right_subtree = heist(root.right)

    include_root = root.data + left_subtree[1] + right_subtree[1]
    exclude_root = max(left_subtree) + max(right_subtree)

    return [include_root, exclude_root]

def rob(root):

    return max(heist(root))
if __name__ == '__main__':

    # Create a list of list of TreeNode objects to represent binary trees
    list_of_trees = [[TreeNode(10), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)],
                     [TreeNode(7), TreeNode(9), TreeNode(10), TreeNode(15), TreeNode(20)],
                     [TreeNode(8), TreeNode(2), TreeNode(17), TreeNode(1), TreeNode(4), TreeNode(19), TreeNode(5)],
                     [TreeNode(7), TreeNode(3), TreeNode(4), TreeNode(1), TreeNode(3)],
                     [TreeNode(9), TreeNode(5), TreeNode(7), TreeNode(1), TreeNode(3)],
                     [TreeNode(9), TreeNode(7), None, None, TreeNode(1), TreeNode(8), TreeNode(10), None, TreeNode(12)]
                     ]

    # Create the binary trees using the BinaryTree class
    input_trees = []
    for list_of_nodes in list_of_trees:
        tree = BinaryTree(list_of_nodes)
        input_trees.append(tree)

    # Print the input trees
    x = 1
    for tree in input_trees:

        x += 1
        print("\tMaximum amount we can rob without getting caught: ", rob(tree.root), sep="")
        print("-" * 100)
