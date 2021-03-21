class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def empty(self):
        return len(self.queue) == 0


class Tree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree_recursively(self):
        print(self.data)

        if self.left != None:
            self.left.print_tree_recursively()

        if self.right != None:
            self.right.print_tree_recursively()

    def print_tree(self):
        q = queue()
        q.enqueue(self)

        while not q.empty():
            front = q.dequeue()
            print(front.data)
            if front.left != None:
                q.enqueue(front.left)
            if front.right != None:
                q.enqueue(front.right)

    def count_level(self):
        if self.data == None:
            return 0

        if (self.left != None) and (self.right != None):

            return max(self.left.count_level(), self.right.count_level()) + 1

        elif (self.left != None) and (self.right == None):
            return self.left.count_level() + 1

        elif (self.left == None) and (self.right != None):
            return self.right.count_level() + 1

        elif (self.left == None) and (self.right == None):
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
root.left = Tree('1')
root.right = Tree('2')
root.left.left = Tree('3')
root.left.right = Tree('4')
root.right.left = Tree('5')
root.right.right = Tree('6')
root.left.left.left = Tree('7')
root.left.left.right = Tree('8')

root.left.right.left = Tree('9')
root.left.right.right = Tree('10')

root.right.left.left = Tree('11')
root.right.left.right = Tree('12')

root.right.right.left = Tree('13')
root.right.right.right = Tree('14')

# root.print_tree_recursively()
print('\n')

root.print_tree()
level = root.count_level()

print('Height of tree is ', level)

all_pieces = root.count_elements()
print('Number of elements of tree is ', all_pieces)