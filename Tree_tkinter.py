from tkinter import *


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


tree = BinaryTree(root)
tree.root.left = Node(left)
tree.root.right = Node(right)

tree.root.left.left = Node(left_left)
tree.root.left.right = Node(left_right)

tree.root.right.left = Node(right_left)
tree.root.right.right = Node(right_right)

window = Tk()

window.geometry('1000x200')

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

label_final = Label(window, text="Result: ").grid(row=10, column=8, sticky=W)

lblresult = Entry(window, justify=RIGHT)
lblresult.grid(row=15, column=8, sticky=E)

btresult1 = Button(window, text="Compute Sum", command=lambda: print_tree_1((root.get(),
                                                                             left.get(),
                                                                             right.get(),
                                                                             left_left.get(),
                                                                             left_right.get(),
                                                                             right_left.get(),
                                                                             right_right.get(),

btresult1.grid(row=19, column=8, sticky=E)



window.mainloop()