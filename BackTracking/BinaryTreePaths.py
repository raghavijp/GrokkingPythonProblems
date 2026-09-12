from BinaryTree import *
from TreeNode import *

def binary_tree_paths(root):
    def backtrackPaths (root, path):
        if root:
            path += str(root.data)
            if not root.left and not root.right:
                paths.append(path)
            else:
                path += '->'
                backtrackPaths(root.left,path)
                backtrackPaths(root.right, path)

    paths = []
    backtrackPaths(root, '')
    return paths

# Driver code
if __name__ == '__main__':
    trees = [[TreeNode(3), TreeNode(2), TreeNode(17), TreeNode(1), None, TreeNode(19), TreeNode(5)],
             [TreeNode(7), TreeNode(6), TreeNode(5), TreeNode(4), TreeNode(3), TreeNode(2), None, TreeNode(1)],
             [TreeNode(5), TreeNode(4), TreeNode(6), TreeNode(3), TreeNode(2), TreeNode(7), TreeNode(8), None, TreeNode(9)],
             [TreeNode(5), TreeNode(2), TreeNode(1), TreeNode(6), TreeNode(10), None, TreeNode(44)],
             [TreeNode(1), TreeNode(2), TreeNode(5), TreeNode(3), TreeNode(4), TreeNode(6)]]

    input_trees = []
    for list_of_nodes in trees:
        tree = BinaryTree(list_of_nodes)
        input_trees.append(tree)

    x = 1
    for i in range(len(input_trees)):
        print(x, ".\tInput Tree:", sep="")
        res = binary_tree_paths(input_trees[i].root)
        print("\n\tPaths:", res)
        x += 1
        print("-" * 100)
