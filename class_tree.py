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

root = Tree('root')
root.left = Tree('left')
root.right = Tree('right')
root.left.left = Tree('left->left')
root.left.left.left = Tree('left->left->left')
root.left.left.right = Tree('left->left->right')
root.left.left.right.right = Tree('left->left->right->right')
root.left.right = Tree('left->right')


print_tree(root)
print('\n')
level = count_level(root)

print(level)