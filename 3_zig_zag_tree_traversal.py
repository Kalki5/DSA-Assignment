class Node:
    left = right = None

    def __init__(self,data):
       self.data = data


def zig_zag_traversal(root_node):
    if root_node is None:
        return

    # Initializing stacks and the direction of the root level
    current_level = []
    next_level = []
    direction = 'left-right'

    # Pushing root node to the current_level stack
    current_level.append(root_node)

    # Iterating till the current_level stack becomes empty
    while len(current_level) > 0:
        # Popping and visiting the last element from the current_level stack
        current_node = current_level.pop(-1)
        print(current_node.data, end=" ")

        # Checking direction and pushing nodes to next_level accordingly
        if direction == 'left-right':
            if current_node.left:
                next_level.append(current_node.left)
            if current_node.right:
                next_level.append(current_node.right)
        elif direction == 'right-left':
            if current_node.right:
                next_level.append(current_node.right)
            if current_node.left:
                next_level.append(current_node.left)

        # Check if it is the last iteration of the current level
        if len(current_level) == 0:
            # Reversing the direction
            if direction == 'right-left':
                direction = 'left-right'
            elif direction == 'left-right':
                direction = 'right-left'

            # Swapping current_level and next_level stack
            # i.e. moving to next level
            current_level, next_level = next_level, current_level


# Constructing the tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Zigzag Order traversal of given Binary tree is: ")
zig_zag_traversal(root)
# 1 3 2 4 5 6 7