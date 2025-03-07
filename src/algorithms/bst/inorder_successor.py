def inorder_successor(root, node):
    if node.right:
        return min_value_node(node.right)

    successor = None
    while root:
        if node.data < root.data:
            successor = root
            root = root.left
        elif node.data > root.data:
            root = root.right
        else:
            break
    return successor

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current