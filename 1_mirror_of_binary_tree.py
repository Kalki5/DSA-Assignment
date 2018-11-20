class Node:
    left = right = None

    def __init__(self,data):
       self.data = data


def mirror(node):
    '''Mirrors the given binary tree'''
    if node:
        # mirror the left sub tree recursively
        mirror(node.left)
        # mirror the right sub tree recursively
        mirror(node.right)
        # Swap the left and right nodes
        node.left, node.right = node.right, node.left


def in_order_traversal(node):
    '''Visit the nodes using in order traversal'''
    if node:
        in_order_traversal(node.left)
        print(node.data, end=' ')
        in_order_traversal(node.right)


# Constructing the tree
root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(7)
root.left.right = Node(9)


print('Inorder traversal of the Tree before mirroring: ')
in_order_traversal(root)
# 1 3 5 7 9

print('\nMirroring the Tree\n')
mirror(root)

print('Inorder traversal of the Tree after mirroring: ')
in_order_traversal(root)
# 1 5 3 9 7