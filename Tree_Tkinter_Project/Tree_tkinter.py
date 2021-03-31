from tkinter import *

from node import *

# creating GUI
window = Tk()
window.geometry('1000x150')
window.title("Tree")


def open_tree_left():
    if var2.get() == 1:
        global left_left
        left_left = IntVar()
        entry4 = Entry(window, textvariable=left_left, justify=RIGHT, width=8).grid(row=3, column=2)

        global left_right
        left_right = IntVar()
        entry5 = Entry(window, textvariable=left_right, justify=RIGHT, width=8).grid(row=3, column=6)


    else:
        entry4 = None
        entry5 = None


def open_tree_right():
    if var3.get() == 1:
        global right_left
        right_left = IntVar()
        entry6 = Entry(window, textvariable=right_left, justify=RIGHT, width=8).grid(row=3, column=10)

        global right_right
        right_right = IntVar()
        entry7 = Entry(window, textvariable=right_right, justify=RIGHT, width=8).grid(row=3, column=14)

    else:
        entry6 = None
        entry7 = None


root = IntVar()
entry1 = Entry(window, textvariable=root, justify=RIGHT, width=8).grid(row=1, column=8)

left = IntVar()
entry2 = Entry(window, textvariable=left, justify=RIGHT, width=8).grid(row=2, column=4)

var2 = IntVar()
c2 = Checkbutton(window, text='More left and right', variable=var2, onvalue=1, offvalue=0, command=open_tree_left).grid(
    row=2, column=5)

right = IntVar()
entry3 = Entry(window, textvariable=right, justify=RIGHT, width=8).grid(row=2, column=12)

var3 = IntVar()
c3 = Checkbutton(window, text='More left and right', variable=var3, onvalue=1, offvalue=0,
                 command=open_tree_right).grid(row=2, column=13)


# left_left = IntVar()
# entry4 = Entry(window, textvariable=left_left, justify=RIGHT, width=8).grid(row=3, column=2)

# left_right = IntVar()
# entry5 = Entry(window, textvariable=left_right, justify=RIGHT, width=8).grid(row=3, column=6)

# right_left = IntVar()
# entry6 = Entry(window, textvariable=right_left, justify=RIGHT, width=8).grid(row=3, column=10)

# right_right = IntVar()
# entry7 = Entry(window, textvariable=right_right, justify=RIGHT, width=8).grid(row=3, column=14)


def create_tree(root, left, right, left_left, left_right, right_left, right_right):
    '''This function creates a tree object from given values
    '''
    tree = BinaryTree(root)

    tree.root.left = Node(left)
    tree.root.right = Node(right)

    tree.root.left.left = Node(left_left) if left_left != 0 else None
    tree.root.left.right = Node(left_right) if left_right != 0 else None

    tree.root.right.left = Node(right_left) if right_left != 0 else None
    tree.root.right.right = Node(right_right) if right_right != 0 else None

    return tree


def binary_search_tree(left_left, left, left_right, root, right_left, right, right_right):
    if not left_left and not left_right and not right_left and not right_right:
        if left < root < right:
            return True
    if left_left < left < left_right < root < right_left < right < right_right:
        return True

    return False


def preorder(root, left, right, left_left, left_right, right_left, right_right):
    '''This function prints objects of root preorderly, root-left-right
    '''
    tree = create_tree(root, left, right, left_left, left_right, right_left, right_right)
    lblresult.delete(0, END)
    lblresult.insert(0, tree.print_tree_1(tree.root, "preorder"))


def inorder(root, left, right, left_left, left_right, right_left, right_right):
    '''This function prints objects of root in order, left-root-right
    '''
    tree = create_tree(root, left, right, left_left, left_right, right_left, right_right)
    lblresult.delete(0, END)
    lblresult.insert(0, tree.print_tree_1(tree.root, "inorder"))

    if binary_search_tree(left_left, left, left_right, root, right_left, right, right_right) is True:
        lbl_binary.delete(0, END)
        lbl_binary.insert(0, 'Yes')
    else:
        lbl_binary.delete(0, END)
        lbl_binary.insert(0, 'No')


def postorder(root, left, right, left_left, left_right, right_left, right_right):
    '''This function prints objects of root postorderly, left-right-root
    '''
    tree = create_tree(root, left, right, left_left, left_right, right_left, right_right)
    lblresult.delete(0, END)
    lblresult.insert(0, tree.print_tree_1(tree.root, "postorder"))


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

window.mainloop()