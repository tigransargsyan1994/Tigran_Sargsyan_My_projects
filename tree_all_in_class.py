class Tree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self):
        print(self.data)

        if self.left != None:
            self.left.print_tree()
        if self.right != None:
            self.right.print_tree()

    def count_level(self):
        if self.data == None:
            return 0

        if (self.left != None) and (self.right != None):
            return max(self.left.count_level(), self.right.count_level()) + 1

        if (self.left == None) and (self.right != None):
            return self.right.count_level() + 1

        if (self.left != None) and (self.right == None):
            return self.left.count_level() + 1


        if (self.left == None) and (self.right == None):
            return 1

    def count_elements(self):
        if self.data == None:
            return 0

        if (self.left != None) and (self.right != None):
            return self.left.count_elements() + self.right.count_elements() + 1

        if (self.left == None) and (self.right != None):
            return self.right.count_elements() + 1

        if (self.left != None) and (self.right == None):
            return self.left.count_elements() + 1

        if (self.left == None) and (self.right == None):
            return 1


root = Tree('root')
root.left = Tree('left')
root.left.left = Tree('left->left')
root.right = Tree('Right')
root.left.right = Tree('left->right')




root.print_tree()
print('\n')
level = root.count_level()
print('Height of tree is', level)
elements = root.count_elements()
print('Number of elements is ', elements)