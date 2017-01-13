class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def bst_checker(root):

    # start at the root, with an arbitrarily low lower bound
    # and an arbitrarily high upper bound
    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    # depth-first traversal
    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        # if this node is invalid, we return false right away
        if (node.value < lower_bound) or (node.value > upper_bound):
            return False

        if node.left:
            # this node must be less than the current node
            node_and_bounds_stack.append((node.left, lower_bound, node.value))
        if node.right:
            # this node must be greater than the current node
            node_and_bounds_stack.append((node.right, node.value, upper_bound))

    # if none of the nodes were invalid, return true
    # (at this point we have checked all nodes)
    return True

def inorder_print(node):
    if node:
        inorder_print(node.left)
        print(node.value)
        inorder_print(node.right)

def find_second_largest_element(bst_root):
    current_node = bst_root

    # Null check
    if not bst_root:
        return candidate

    while current_node.right:
        prev_node = current_node
        current_node = current_node.right

    if current_node.left:
        return current_node.value
    else:
        return prev_node.value


# Create a BST
bst = BinaryTreeNode(7)
bst.left = BinaryTreeNode(3)
bst.left.left = BinaryTreeNode(2)
bst.left.left.left = BinaryTreeNode(1)
bst.left.right = BinaryTreeNode(5)
bst.left.right.left = BinaryTreeNode(4)
bst.left.right.right = BinaryTreeNode(6)
bst.right = BinaryTreeNode(8)
bst.right.right = BinaryTreeNode(9)
bst.right.right.right = BinaryTreeNode(10)

print(find_second_largest_element(bst))
