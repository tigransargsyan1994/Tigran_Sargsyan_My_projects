from tkinter import *

from bst_import import *

def check_binary(root, left, right, left_left, left_right, right_left, right_right):
    tree = create_tree(root, left, right, left_left, left_right, right_left, right_right)

    if isbst(tree):
        lbl_binary.delete(0, END)
        lbl_binary.insert(0, "is BST")
    else:
        lbl_binary.delete(0, END)
        lbl_binary.insert(0, "not a BST")


def create_tree(root, left, right, left_left, left_right, right_left, right_right):
    '''This function creates a tree object from given values
    '''
    tree = Node(root)

    tree.left = Node(left)
    tree.right = Node(right)

    tree.left.left = Node(left_left) if left_left != 0 else None
    tree.left.right = Node(left_right) if left_right != 0 else None

    tree.right.left = Node(right_left) if right_left != 0 else None
    tree.right.right = Node(right_right) if right_right != 0 else None

    return tree


def preorder(root, left, right, left_left, left_right, right_left, right_right):
    '''This function prints objects of root preorderly, root-left-right
    '''
    tree = create_tree(root, left, right, left_left, left_right, right_left, right_right)
    lblresult.delete(0, END)
    lblresult.insert(0, tree.print_tree_1(tree, "preorder"))


def inorder(root, left, right, left_left, left_right, right_left, right_right):
    '''This function prints objects of root in order, left-root-right
    '''
    tree = create_tree(root, left, right, left_left, left_right, right_left, right_right)
    lblresult.delete(0, END)
    lblresult.insert(0, tree.print_tree_1(tree, "inorder"))


def postorder(root, left, right, left_left, left_right, right_left, right_right):
    '''This function prints objects of root postorderly, left-right-root
    '''
    tree = create_tree(root, left, right, left_left, left_right, right_left, right_right)
    lblresult.delete(0, END)
    lblresult.insert(0, tree.print_tree_1(tree, "postorder"))



window = Tk()
window.geometry('1000x250')
window.title("Tree")

root = IntVar()
entry1 = Entry(window, textvariable=root, justify=RIGHT, width=8).grid(row=1, column=8)

left = IntVar()
entry2 = Entry(window, textvariable=left, justify=RIGHT, width=8).grid(row=2, column=4)

right = IntVar()
entry3 = Entry(window, textvariable=right, justify=RIGHT, width=8).grid(row=2, column=12)

left_left = IntVar()
entry4 = Entry(window, textvariable=left_left, justify=RIGHT, width=8).grid(row=3, column=2)

left_right = IntVar()
entry5 = Entry(window, textvariable=left_right, justify=RIGHT, width=8).grid(row=3, column=6)

right_left = IntVar()
entry6 = Entry(window, textvariable=right_left, justify=RIGHT, width=8).grid(row=3, column=10)

right_right = IntVar()
entry7 = Entry(window, textvariable=right_right, justify=RIGHT, width=8).grid(row=3, column=14)

label_final = Label(window, text="Result: ").grid(row=10, column=8, sticky=N)

label_binary_search = Label(window, text="Binary_search: ").grid(row=12, column=12, sticky=N)

lbl_binary = Entry(window, justify=RIGHT, width=8)

lbl_binary.grid(row=13, column=12, sticky=N)

lblresult = Entry(window, justify=RIGHT, width=40)

lblresult.grid(row=11, column=8, sticky=E)

btresult1 = Button(window, text="Pre_Order", command=lambda: preorder(root.get(),
                                                                      left.get(),
                                                                      right.get(),
                                                                      left_left.get(),
                                                                      left_right.get(),
                                                                      right_left.get(),
                                                                      right_right.get()))

btresult1.grid(row=12, column=8, sticky=W)
btresult2 = Button(window, text="In_Order", command=lambda: inorder(root.get(),
                                                                    left.get(),
                                                                    right.get(),
                                                                    left_left.get(),
                                                                    left_right.get(),
                                                                    right_left.get(),
                                                                    right_right.get()))

btresult2.grid(row=12, column=8, sticky=N)
btresult3 = Button(window, text="Post_Order", command=lambda: postorder(root.get(),
                                                                        left.get(),
                                                                        right.get(),
                                                                        left_left.get(),
                                                                        left_right.get(),
                                                                        right_left.get(),
                                                                        right_right.get()))

btresult3.grid(row=12, column=8, sticky=E)

btresult4 = Button(window, text="Is Binary Search Tree or not", command=lambda: check_binary(root.get(),
                                                                                             left.get(),
                                                                                             right.get(),
                                                                                             left_left.get(),
                                                                                             left_right.get(),
                                                                                             right_left.get(),
                                                                                             right_right.get()))

btresult4.grid(row=14, column=12, sticky=E)

window.mainloop()