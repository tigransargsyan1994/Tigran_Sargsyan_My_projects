from tkinter import *

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


def import111(root, left, right, left_left, left_right, right_left, right_right):
    num1 = root
    num2 = left
    num3 = right
    num4 = left_left
    num5 = left_right
    num6 = right_left
    num7 = right_right

    class Node(object):
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value

    class BinaryTree(object):
        def __init__(self, root):
            self.root = Node(root)

        def print_tree_1(self, traversal_type):
            if traversal_type == 'preorder':
                return self.preorder_print(tree.root, '')

        def preorder_print(self, start, traversal):
            if start:
                traversal += (str(start.value) + ' - ')
                traversal = self.preorder_print(start.left, traversal)
                traversal = self.preorder_print(start.right, traversal)
            return traversal

    tree = BinaryTree(num1)

    tree.root.left = Node(num2)
    tree.root.right = Node(num3)

    tree.root.left.left = Node(num4)
    tree.root.left.right = Node(num5)

    tree.root.right.left = Node(num6)
    tree.root.right.right = Node(num7)

    lblresult.delete(0, END)
    lblresult.insert(0, tree.print_tree_1('preorder'))


def import222(root, left, right, left_left, left_right, right_left, right_right):
    num1 = root
    num2 = left
    num3 = right
    num4 = left_left
    num5 = left_right
    num6 = right_left
    num7 = right_right

    class Node(object):
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value

    class BinaryTree(object):
        def __init__(self, root):
            self.root = Node(root)

        def print_tree_1(self, traversal_type):

            if traversal_type == 'inorder':
                return self.inorder_print(tree.root, '')

        def inorder_print(self, start, traversal):
            if start:
                traversal = self.inorder_print(start.left, traversal)
                traversal += (str(start.value) + ' - ')
                traversal = self.inorder_print(start.right, traversal)

            return traversal

    tree = BinaryTree(num1)

    tree.root.left = Node(num2)
    tree.root.right = Node(num3)

    tree.root.left.left = Node(num4)
    tree.root.left.right = Node(num5)

    tree.root.right.left = Node(num6)
    tree.root.right.right = Node(num7)

    lblresult.delete(0, END)
    lblresult.insert(0, tree.print_tree_1('inorder'))


def import333(root, left, right, left_left, left_right, right_left, right_right):
    num1 = root
    num2 = left
    num3 = right
    num4 = left_left
    num5 = left_right
    num6 = right_left
    num7 = right_right

    class Node(object):
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value

    class BinaryTree(object):
        def __init__(self, root):
            self.root = Node(root)

        def print_tree_1(self, traversal_type):

            if traversal_type == 'postorder':
                return self.postorder_print(tree.root, '')

        def postorder_print(self, start, traversal):
            if start:
                traversal = self.postorder_print(start.left, traversal)
                traversal = self.postorder_print(start.right, traversal)
                traversal += (str(start.value) + ' - ')

            return traversal

    tree = BinaryTree(num1)

    tree.root.left = Node(num2)
    tree.root.right = Node(num3)

    tree.root.left.left = Node(num4)
    tree.root.left.right = Node(num5)

    tree.root.right.left = Node(num6)
    tree.root.right.right = Node(num7)

    lblresult.delete(0, END)
    lblresult.insert(0, tree.print_tree_1('postorder'))


label_final = Label(window, text="Result: ").grid(row=10, column=8, sticky=N)

lblresult = Entry(window, justify=RIGHT, width=50)
lblresult.grid(row=15, column=8, sticky=E)

btresult1 = Button(window, text="Pre_Order", command=lambda: import111(root.get(),
                                                                       left.get(),
                                                                       right.get(),
                                                                       left_left.get(),
                                                                       left_right.get(),
                                                                       right_left.get(),
                                                                       right_right.get()))

btresult1.grid(row=19, column=8, sticky=W)

btresult2 = Button(window, text="In_Order", command=lambda: import222(root.get(),
                                                                      left.get(),
                                                                      right.get(),
                                                                      left_left.get(),
                                                                      left_right.get(),
                                                                      right_left.get(),
                                                                      right_right.get()))

btresult2.grid(row=19, column=8, sticky=N)

btresult3 = Button(window, text="Post_Order", command=lambda: import333(root.get(),
                                                                        left.get(),
                                                                        right.get(),
                                                                        left_left.get(),
                                                                        left_right.get(),
                                                                        right_left.get(),
                                                                        right_right.get()))

btresult3.grid(row=19, column=8, sticky=E)

window.mainloop()