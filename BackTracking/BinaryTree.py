from typing import List
from queue import Queue
from .TreeNode import TreeNode

class BinaryTree:
    def __init__(self, nodes):
        self.root = self.createBinaryTree(nodes)

    def createBinaryTree(self, nodes):
        if len(nodes) == 0:
            return None

        root = TreeNode(nodes[0].data)

        queue = Queue()
        queue.put(root)

        i = 1
        while i < len(nodes):

            curr = queue.get()

            if nodes[i] is not None:
                curr.left = TreeNode(nodes[i].data)
                queue.put(curr.left)

            i +=1

            if i < len(nodes) and nodes[i] is not None:
                curr.right = TreeNode(nodes[i].data)
                queue.put(curr.right)

            i+=1

        return root


