
class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self):
        return self.preorder_print(tree.root, '')


    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + ' - ')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree())