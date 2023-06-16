class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode(10)
node = TreeNode(7)
c_node = root
c_node.left = node
c_node.right = TreeNode(12)
c_node = node
c_node.right = TreeNode(8)
c_node.left = TreeNode(5)
c_node = c_node.right
c_node.right = TreeNode(9)

def print_node(node):
    print(node.value)
    if node.left is not None:
        print_node(node.left)
    if node.right is not None:
        print_node(node.right)

print_node(root)