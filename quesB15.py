# 15.Count the total number of nodes present in a binary tree.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count_nodes(root):
    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)


root = Node(50)
root.left = Node(30)
root.right = Node(70)

print("Total Nodes:", count_nodes(root))