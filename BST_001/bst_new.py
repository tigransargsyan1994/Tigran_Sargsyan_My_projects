import tkinter as tk
import tkinter.ttk as ttk
from inorder_preorder_postorder import *


class Application(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.initialize_user_interface()
        self.list1 = []

    def initialize_user_interface(self):
        # Configure the root object for the Application
        self.root.title("Application")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.config(background="green")

        # Define the different GUI widgets
        self.name_label = tk.Label(self.root, text="Node:")
        self.name_label.grid(row=0, column=0, sticky='W')
        self.element_entry = tk.Entry(self.root, width=10)
        self.element_entry.grid(row=0, column=1, sticky='E')

        self.name_label_preorder = tk.Label(self.root, text="Preorder:")
        self.name_label_preorder.grid(row=1, column=0, sticky='W')
        self.element_result_preorder = tk.Entry(self.root, width=40)
        self.element_result_preorder.grid(row=1, column=1, sticky='E')

        self.name_label_inorder = tk.Label(self.root, text="Inorder:")
        self.name_label_inorder.grid(row=2, column=0, sticky='W')
        self.element_result_inorder = tk.Entry(self.root, width=40)
        self.element_result_inorder.grid(row=2, column=1, sticky='E')

        self.name_label_postorder = tk.Label(self.root, text="Postorder:")
        self.name_label_postorder.grid(row=3, column=0, sticky='W')
        self.element_result_postorder = tk.Entry(self.root, width=40)
        self.element_result_postorder.grid(row=3, column=1, sticky='E')

        self.submit_button_insert = tk.Button(self.root,
                                              text="Insert_element",
                                              command=lambda: [self.insert_element(), self.add_to_list()])
        self.submit_button_insert.grid(row=0, column=2, sticky='e')

        self.submit_button_preorder = tk.Button(self.root,
                                                text="Preorder",
                                                command=self.make_preordered)
        self.submit_button_preorder.grid(row=1, column=2, sticky='e')

        self.submit_button_inorder = tk.Button(self.root,
                                               text="Inorder",
                                               command=self.make_inordered)
        self.submit_button_inorder.grid(row=2, column=2, sticky='e')

        self.submit_button_postorder = tk.Button(self.root,
                                                 text="Postorder",
                                                 command=self.make_postordered)
        self.submit_button_postorder.grid(row=3, column=2, sticky='e')

        # Set the treeview
        self.tree = ttk.Treeview(self.root, columns=('Elements'))

        # Set the heading (Attribute Names)
        self.tree.heading('#0', text='Item')
        self.tree.heading('#1', text='Elements')

        # Specify attributes of the columns (We want to stretch it!)
        self.tree.column('#0', stretch=tk.YES)
        self.tree.column('#1', stretch=tk.YES)

        self.tree.grid(row=4, columnspan=3, sticky='nsew')
        self.treeview = self.tree

        self.id = 0
        self.iid = 0

    def add_to_list(self):
        '''
        Adding all the elements of the entry to the list
        '''
        try:
            self.list1.append(int(self.element_entry.get()))
        except ValueError:
            pass

    def insert_element(self):
        '''
        Printing all the elements in entry in Treeview
        '''

        try:
            self.treeview.insert('', 'end', iid=self.iid, text="Item_" + str(self.id),
                                 values=(int(self.element_entry.get())))
        except ValueError:
            pass

        self.iid = self.iid + 1
        self.id = self.id + 1

    def make_preordered(self):
        '''
        Making preordered view of tree
        '''
        try:
            r = Node(self.list1[0])
            for i in app.list1[1:]:
                r = insert(r, i)
            self.element_result_preorder.insert(0, preorder(r))
        except IndexError:
            pass

    def make_inordered(self):
        '''
        Making inordered view of tree
        '''
        try:
            r = Node(self.list1[0])
            for i in app.list1[1:]:
                r = insert(r, i)
            self.element_result_inorder.insert(0, inorder(r))
        except IndexError:
            pass

    def make_postordered(self):
        '''
        Making postordered view of tree
        '''
        try:
            r = Node(self.list1[0])
            for i in app.list1[1:]:
                r = insert(r, i)
            self.element_result_postorder.insert(0, postorder(r))
        except IndexError:
            pass


app = Application(tk.Tk())
app.root.mainloop()