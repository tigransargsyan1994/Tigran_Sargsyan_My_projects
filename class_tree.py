class Tree(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def print_tree(node):
    if node == None:
        return

    print(node.data)
    print_tree(node.left)
    print_tree(node.right)


def count_level(node):
    if node == None:
        return 0

    return max(count_level(node.left), count_level(node.right)) + 1


def count_elements(node):
    if node == None:
        return 0

    return count_elements(node.left) + count_elements(node.right) + 1

root = Tree('root')
root.left = Tree('left')
root.left.left = Tree('left->left')
root.right = Tree('right')
root.left.right = Tree('left->right')


print_tree(root)
print('\n')

level = count_level(root)
print('Height of tree is', level)

elements = count_elements(root)
print('Number of elements is ', elements)