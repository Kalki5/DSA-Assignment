class Node:
    left = right = None
    def __init__(self,data):
       self.data = data


def build_tree(in_order, post_order):
    '''Build Unique Binary Tree from In-Order and Post-Order Traversal'''
    # In-Order is mandatory for building unique tree
    if in_order is None:
        return None

    # Defining sub-function for doing recursion
    def get_tree(i, j, k):

        # If Offset is zero, return None
        if k <= 0:
            return
        
        # Get the node's value by using the end position and the offset
        node = Node(post_order[j + k - 1])

        # Get index of the element from In-Order Traversal
        index = in_order.index(post_order[ j + k - 1])
        
        # Recursively call the function to build left and right subtree
        node.left = get_tree(i, j, index - i)
        node.right = get_tree(index + 1, j - i + index, k - 1 - (index-i))
        return node

    root_node = get_tree(0, 0, len(in_order))
    return root_node


# In-Order and Post-Order sequences defined as an array
in_order_traversal    = [4, 2, 5, 1, 6, 7, 3, 8]
post_order_traversal  = [4, 5, 2, 6, 7, 8, 3, 1]

# Building the binary tree
binary_tree  = build_tree(in_order_traversal, post_order_traversal)

print(binary_tree)