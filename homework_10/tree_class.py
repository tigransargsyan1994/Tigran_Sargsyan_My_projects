class Tree(object):
    def __init__(self, left, right, data):
        self.left = left
        self.right = right
        self.data = data

root = Tree('left', 'right', 'data')
root.data = "root"
root.left = Tree('left', 'right', 'data')
root.left.data = "left"
root.right = Tree('left', 'right', 'data')
root.right.data = "right"

print(root.left.data)

