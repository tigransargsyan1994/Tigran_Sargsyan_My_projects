# Python program to demonstrate
# insert operation in binary search tree

# A utility class that represents
# an individual node in a BST


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


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
def inorder(root):
    global result1
    if root:
        inorder(root.left)
        result1 += str(root.val) + ' '
        inorder(root.right)

    return result1


result2 = ''
def preorder(root):
    global result2
    if root:
        result2 += str(root.val) + ' '
        preorder(root.left)
        preorder(root.right)
    return result2


result3 = ''
def postorder(root):
    global result3
    if root:
        postorder(root.left)
        postorder(root.right)
        result3 += str(root.val) + ' '
    return result3


# result4 = []
# def binary(root):
#     global result4
#     if root:
#         binary(root.left)
#         result4.append(int(root.val))
#         binary(root.right)
#
#     #     return result4
#     for i in range(len(result4) - 1):
#         if result4[i] < result4[i + 1]:
#             continue
#         else:
#             return False
#     return True


# r = Node(50)
# r = insert(r, 25)
# r = insert(r, 45)
# r = insert(r, 121)
# r = insert(r, 3)
# r = insert(r, 856)
# r = insert(r, 87)
#
# # # Print inoder traversal of the BST
# z1 = inorder(r)
# # print()
# z2 = preorder(r)
# # print()
# z3 = postorder(r)
#
# z4 = binary(r)
#
# print(z1)
# print(z2)
# print(z3)
# print(z4)