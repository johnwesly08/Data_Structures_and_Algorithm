class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def in_order_traversal(root):
    if root:
        # Traverse the left subtree
        in_order_traversal(root.left)
        # Visit the root node
        print(root.val, end=" ")
        # Traverse the right subtree
        in_order_traversal(root.right)

def pre_order_traversal(root):
    if root:
        # Visit the root node
        print(root.val, end=" ")
        # Traverse the left subtree
        pre_order_traversal(root.left)
        # Traverse the right subtree
        pre_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        # Traverse the left subtree
        post_order_traversal(root.left)
        # Traverse the right subtree
        post_order_traversal(root.right)
        # Visit the root node
        print(root.val, end=" ")

# Example of creating a simple binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("In-order Traversal:")
in_order_traversal(root)
print("\n")

print("Pre-order Traversal:")
pre_order_traversal(root)
print("\n")

print("Post-order Traversal:")
post_order_traversal(root)
print("\n")
