# Python code to insert a node in AVL tree

# Generic tree node class
class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

    def count_level(self):
        if self.val == None:
            return 0

        if (self.left != None) and (self.right != None):

            return max(self.left.count_level(), self.right.count_level()) + 1

        elif (self.left != None) and (self.right == None):
            return self.left.count_level() + 1

        elif (self.left == None) and (self.right != None):
            return self.right.count_level() + 1

        elif (self.left == None) and (self.right == None):
            return 1


# AVL tree class which supports the
# Insert operation
class AVL_Tree(object):

    # Recursive function to insert key in
    # subtree rooted with node and returns
    # new root of subtree.
    def insert(self, root, key):

        # Step 1 - Perform normal BST
        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # Step 3 - Get the balance factor
        balance = self.get_balance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)

        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)

        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        # Return the new root
        return y

    def right_rotate(self, z):

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        # Return the new root
        return y

    def get_height(self, root):
        if not root:
            return 0

        return root.height

    def get_balance(self, root):
        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)


# Driver program to test above function
tree_instance = AVL_Tree()


result1 = ''
def preorder(root, child=False):
    global result1
    if not child:
        result1 = ''
    if root:
        result1 += str(root.val) + ' '
        preorder(root.left, child=True)
        preorder(root.right, child=True)
    return result1


result2 = ''
def inorder(root, child=False):
    global result2
    if not child:
        result2 = ''
    if root:
        inorder(root.left, child=True)
        result2 += str(root.val) + ' '
        inorder(root.right, child=True)
    return result2


result3 = ''
def postorder(root, child=False):
    global result3
    if not child:
        result3 = ''
    if root:
        postorder(root.left, child=True)
        postorder(root.right, child=True)
        result3 += str(root.val) + ' '
    return result3

# root = myTree.insert(root, 10)
# root = myTree.insert(root, 20)
# root = myTree.insert(root, 30)
# root = myTree.insert(root, 40)
# root = myTree.insert(root, 50)
# root = myTree.insert(root, 25)

# """The constructed AVL Tree would be
#             30
#            /  \
#          20   40
#         /  \     \
#        10  25    50"""

# Preorder Traversal
# print("Preorder traversal of the",
#       "constructed AVL tree is")
# myTree.preorder(root)
# print()

# This code is contributed by Ajitesh Pathak