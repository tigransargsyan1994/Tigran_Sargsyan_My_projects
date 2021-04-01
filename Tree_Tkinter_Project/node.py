class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

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
            traversal += (str(start.value) + ' - ')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + ' - ')
            traversal = self.inorder_print(start.right, traversal)

        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + ' - ')

        return traversal