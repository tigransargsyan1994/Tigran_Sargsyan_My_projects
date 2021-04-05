class Node:
    # constructor to create new node
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def print_tree_1(self, start, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(start, '')
        elif traversal_type == 'inorder':
            return self.inorder_print(start, '')
        elif traversal_type == 'postorder':
            return self.postorder_print(start, '')
        else:
            print('Traversal type' + str(traversal_type) + 'is not supported')

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.data) + ' - ')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.data) + ' - ')
            traversal = self.inorder_print(start.right, traversal)

        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.data) + ' - ')

        return traversal


# global variable prev - to keep track
# of previous node during Inorder
# traversal
prev = None


# function to check if given binary
# tree is BST
def isbst(root):
    # prev is a global variable
    global prev
    prev = None
    return isbst_rec(root)


# Helper function to test if binary
# tree is BST
# Traverse the tree in inorder fashion
# and keep track of previous node
# return true if tree is Binary
# search tree otherwise false

def isbst_rec(root):
    # prev is a global variable
    global prev

    # if tree is empty return true
    if root is None:
        return True

    if isbst_rec(root.left) is False:
        return False

    # if previous node'data is found
    # greater than the current node's
    # data return fals
    if prev is not None and prev.data > root.data:
        return False

    # store the current node in prev
    prev = root
    return isbst_rec(root.right)


