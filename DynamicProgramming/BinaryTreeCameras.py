from BackTracking.TreeNode import TreeNode
from BackTracking.BinaryTree import BinaryTree

def recurse(node):

    if not node:
        return [0, 0, float('inf')]

    L = recurse(node.left)
    R = recurse(node.right)

    # Calculate the minimum cost to cover each child
    # (whether it has a camera or not)
    leftCost = min(L[1], L[2])
    rightCost = min(R[1], R[2])

    # Compute the cost when the current node is not covered
    # (both children must be in state 1)
    dp0 = L[1] + R[1]

    # Compute the cost when the current node is covered without a camera
    # (At least one child must have a camera)
    dp1 = min(L[2] + rightCost , R[2] + leftCost)

    # Compute the cost when the current node has a camera
    dp2 = 1 + min (L[0], leftCost) + min(R[0], rightCost)

    dp0 = min(dp0, float('inf'))
    dp1 = min(dp1, float('inf'))
    dp2 = min(dp2, float('inf'))

    return [dp0, dp1, dp2]

def minimum_cameras(tree):
    res = recurse(tree)

    return min(res[1], res[2])


def main():
    trees = [
        [TreeNode(0), None, TreeNode(0), TreeNode(0), TreeNode(0)],
        [TreeNode(0), TreeNode(0), TreeNode(0), TreeNode(0), TreeNode(0), TreeNode(0), TreeNode(0)],
        [TreeNode(0)],
        [TreeNode(0), TreeNode(0), None, TreeNode(0)],
        [TreeNode(0), TreeNode(0), None, None, TreeNode(0), TreeNode(0), None, None, TreeNode(0)],
    ]

    for i, node_list in enumerate(trees):
        tree = BinaryTree(node_list)
        print(f"\t Minimum cameras needed: ", minimum_cameras(tree.root))

if __name__ == "__main__":
    main()