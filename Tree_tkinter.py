from tkinter import *

# move to another python module and import here
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

# creating GUI
window = Tk()
window.geometry('1100x150')
window.title("Tree")

root = IntVar()
entry1 = Entry(window, textvariable=root, justify=RIGHT).grid(row=1, column=8)

left = IntVar()
entry2 = Entry(window, textvariable=left, justify=RIGHT).grid(row=2, column=4)

right = IntVar()
entry3 = Entry(window, textvariable=right, justify=RIGHT).grid(row=2, column=12)

left_left = IntVar()
entry4 = Entry(window, textvariable=left_left, justify=RIGHT).grid(row=3, column=2)

left_right = IntVar()
entry5 = Entry(window, textvariable=left_right, justify=RIGHT).grid(row=3, column=6)

right_left = IntVar()
entry6 = Entry(window, textvariable=right_left, justify=RIGHT).grid(row=3, column=10)

right_right = IntVar()
entry7 = Entry(window, textvariable=right_right, justify=RIGHT).grid(row=3, column=14)


def create_tree(root, left, right, left_left, left_right, right_left, right_right):
    tree = BinaryTree(root)

    tree.root.left = Node(left)
    tree.root.right = Node(right)

    tree.root.left.left = Node(left_left)
    tree.root.left.right = Node(left_right)

    tree.root.right.left = Node(right_left)
    tree.root.right.right = Node(right_right)

    return tree

def preorder(root, left, right, left_left, left_right, right_left, right_right):
    tree = create_tree(root, left, right, left_left, left_right, right_left, right_right)
    lblresult.delete(0, END)
    lblresult.insert(0, tree.print_tree_1(tree.root, "preorder"))

def inorder(root, left, right, left_left, left_right, right_left, right_right):
    tree = create_tree(root, left, right, left_left, left_right, right_left, right_right)
    lblresult.delete(0, END)
    lblresult.insert(0, tree.print_tree_1(tree.root, "inorder"))

def postorder(root, left, right, left_left, left_right, right_left, right_right):
    tree = create_tree(root, left, right, left_left, left_right, right_left, right_right)
    lblresult.delete(0, END)
    lblresult.insert(0, tree.print_tree_1(tree.root, "postorder"))


label_final = Label(window, text="Result: ").grid(row=10, column=8, sticky=N)

lblresult = Entry(window, justify=RIGHT, width=50)

lblresult.grid(row=15, column=8, sticky=E)
btresult1 = Button(window, text="Pre_Order", command=lambda: preorder(root.get(),
                                                                       left.get(),
                                                                       right.get(),
                                                                       left_left.get(),
                                                                       left_right.get(),
                                                                       right_left.get(),
                                                                       right_right.get()))

btresult1.grid(row=19, column=8, sticky=E)
btresult2 = Button(window, text="In_Order", command=lambda: inorder(root.get(),
                                                                      left.get(),
                                                                      right.get(),
                                                                      left_left.get(),
                                                                      left_right.get(),
                                                                      right_left.get(),
                                                                      right_right.get()))

btresult2.grid(row=19, column=8, sticky=N)
btresult3 = Button(window, text="Post_Order", command=lambda: postorder(root.get(),
                                                                        left.get(),
                                                                        right.get(),
                                                                        left_left.get(),
                                                                        left_right.get(),
                                                                        right_left.get(),
                                                                        right_right.get()))

btresult3.grid(row=19, column=8, sticky=W)

window.mainloop()
