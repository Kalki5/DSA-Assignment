class Node:
    left = right = None
    def __init__(self, data=None):
       self.data = data

    def insert(self, data):
        '''Insert new data to this BST'''
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data >= self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


def in_order_traversal(node):
    '''Visit the nodes using in order traversal'''
    if node:
        yield from in_order_traversal(node.left)
        yield node.data
        yield from in_order_traversal(node.right)


# CASE 1
# Constructing BST A
bst_1a = Node()
for i in [10, 5, 20, 15, 30]:
    bst_1a.insert(i)

# Constructing BST B
bst_1b = Node()
for i in [10, 20, 15, 30, 5]:
    bst_1b.insert(i)

# InOrder Traversing of CASE 1 BSTs
bst_1a_iot = list(in_order_traversal(bst_1a))
bst_1b_iot = list(in_order_traversal(bst_1b))

# Comparing CASE 1 BSTs to check if they are same
print(bst_1a_iot, '==', bst_1b_iot, '\t--->', bst_1a_iot == bst_1b_iot)
# [5, 10, 15, 20, 30] == [5, 10, 15, 20, 30]      ---> True


# CASE 2
# Constructing BST A
bst_2a = Node()
for i in [10, 5, 20, 15, 30]:
    bst_2a.insert(i)

# Constructing BST B
bst_2b = Node()
for i in [10, 5, 30, 20, 5]:
    bst_2b.insert(i)

# InOrder Traversing of CASE 2 BSTs
bst_2a_iot = list(in_order_traversal(bst_2a))
bst_2b_iot = list(in_order_traversal(bst_2b))

# Comparing CASE 2 BSTs to check if they are same
print(bst_2a_iot, '==', bst_2b_iot, '\t--->', bst_2a_iot == bst_2b_iot)
# [5, 10, 15, 20, 30] == [5, 5, 10, 20, 30]       ---> False