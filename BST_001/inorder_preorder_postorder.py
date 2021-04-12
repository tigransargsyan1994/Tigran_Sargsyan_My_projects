# Python program to demonstrate
# insert operation in binary search tree

# A utility class that represents
# an individual node in a BST


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

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


# A utility function to insert
# a new node with the given key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


# A utility function to do inorder tree traversal

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

# result1 = ''
# def preorder(root, result2):
#     if root:
#         result1 += str(root.val)
#         result1 = preorder(root.left, result1)
#         result1 = preorder(root.right, result1)
#     return result1


# result2 = ''
# def inorder(root, result1):
#     if root:
#         result2 = inorder(root.left, result2)
#         result2 += str(root.val)
#         result2 = inorder(root.right, result2)
#     return result2


# result3 = ''
# def postorder(root, result3):
#     if root:

#         result3 = postorder(root.left, result3)
#         result3 = postorder(root.right, result3)
#         result3 += str(root.val)
#     return result3