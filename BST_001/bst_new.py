import tkinter as tk
import tkinter.ttk as ttk
from inorder_preorder_postorder import *


class Application(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.initialize_user_interface()

    def initialize_user_interface(self):
        # Configure the root object for the Application
        self.root.title("Application")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.config(background="green")
        self.root.geometry('370x720')

        # Define the different GUI widgets
        self.element_entry = tk.Entry(self.root, width=10)
        self.element_entry.grid(row=0, column=0, sticky='w', padx=2)

        self.element_result_preorder = tk.Entry(self.root, width=40)
        self.element_result_preorder.grid(row=1, column=0, sticky='w', padx=2)

        self.element_result_inorder = tk.Entry(self.root, width=40)
        self.element_result_inorder.grid(row=2, column=0, sticky='w', padx=2)

        self.element_result_postorder = tk.Entry(self.root, width=40)
        self.element_result_postorder.grid(row=3, column=0, sticky='w', padx=2)

        self.element_result_count = tk.Entry(self.root, width=40)
        self.element_result_count.grid(row=4, column=0, sticky='w', padx=2)

        self.element_result_height = tk.Entry(self.root, width=40)
        self.element_result_height.grid(row=5, column=0, sticky='w', padx=2)

        '''Creating buttons
        '''
        self.submit_button_insert = tk.Button(self.root,
                                              text="Insert",
                                              command=lambda: [self.insert_element()])
        self.submit_button_insert.grid(row=0, column=2, sticky='e', padx=2, pady=2)

        self.submit_button_preorder = tk.Button(self.root,
                                                text="Preorder",
                                                command=self.make_preordered)
        self.submit_button_preorder.grid(row=1, column=2, sticky='e', padx=2, pady=2)

        self.submit_button_inorder = tk.Button(self.root,
                                               text="Inorder",
                                               command=self.make_inordered)
        self.submit_button_inorder.grid(row=2, column=2, sticky='e', padx=2, pady=2)

        self.submit_button_postorder = tk.Button(self.root,
                                                 text="Postorder",
                                                 command=self.make_postordered)
        self.submit_button_postorder.grid(row=3, column=2, sticky='e', padx=2, pady=2)

        self.submit_button_count = tk.Button(self.root,
                                             text="Count",
                                             command=self.count_elements)
        self.submit_button_count.grid(row=4, column=2, sticky='e', padx=2, pady=2)

        self.submit_button_height = tk.Button(self.root,
                                              text="Height",
                                              command=self.measure_level)
        self.submit_button_height.grid(row=5, column=2, sticky='e', padx=2, pady=2)

        self.submit_button_height = tk.Button(self.root,
                                              text="Clear space",
                                              command=lambda: [self.refresh_treeview()])
        self.submit_button_height.grid(row=7, column=2, sticky='e', padx=2, pady=2)

        self.tree = ttk.Treeview(self.root, columns=('Elements'))

        self.verscrlbar = ttk.Scrollbar(self.tree,
                                        orient="vertical",
                                        command=self.tree.yview)
        self.verscrlbar.pack(side='right', fill='y', ipadx=1, ipady=230, padx=1, pady=1)

        # Set the heading (Attribute Names)
        self.tree.heading('#0', text='Item')
        self.tree.heading('#1', text='Elements')

        self.tree.grid(row=8, columnspan=3, sticky='nsew')
        self.treeview = self.tree

        self.id = 0
        self.iid = 0

    def insert_element(self):
        '''
        Printing all the elements in entry in Treeview
        '''
        iid = self.iid,

        try:
            self.tree.insert('', 'end', text="Item_" + str(self.id),
                             values=(int(self.element_entry.get())))
            self.iid = self.iid + 1
            self.id = self.id + 1
        except ValueError:
            pass

    def make_tree_from_treeview(self):
        '''Makes binary tree from elements of TreeView
        '''
        z = []
        for child in self.tree.get_children():
            z.append(self.tree.item(child)['values'])
        z = [i[0] for i in z]
        r = Node(z[0])
        for i in z[1:]:
            r = myTree.insert(r, i)
        return r

    def make_preordered(self):
        '''
        Making preordered view of tree
        '''

        try:
            r = self.make_tree_from_treeview()
            self.element_result_preorder.delete(0, tk.END)
            self.element_result_preorder.insert(0, preorder(r))

        except IndexError:
            pass

    def make_inordered(self):
        '''
        Making inordered view of tree
        '''
        try:
            r = self.make_tree_from_treeview()
            self.element_result_inorder.delete(0, 'end')
            self.element_result_inorder.insert(0, inorder(r))
        except IndexError:
            pass

    def make_postordered(self):
        '''
        Making postordered view of tree
        '''
        try:
            r = self.make_tree_from_treeview()
            self.element_result_postorder.delete(0, 'end')
            self.element_result_postorder.insert(0, postorder(r))
        except IndexError:
            pass

    def count_elements(self):
        '''Counting number of elements
        '''
        try:
            self.element_result_count.delete(0, 'end')
            self.element_result_count.insert(0, len(self.tree.get_children()))
        except IndexError:
            pass

    def measure_level(self):
        '''Measuring height of tree
        '''
        try:
            r = self.make_tree_from_treeview()
            self.element_result_height.delete(0, 'end')
            self.element_result_height.insert(0, Node.count_level(r))

        except IndexError:
            pass

    def refresh_treeview(self):
        """
        Clears the Treeview and repopulates it with the current contents of the tree.
        """
        # clear the entries in the Treeview
        for x in self.tree.get_children():
            self.tree.delete(x)
        self.iid = 0
        self.id = 0


app = Application(tk.Tk())
app.root.mainloop()