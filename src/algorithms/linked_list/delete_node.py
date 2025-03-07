class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_node(node):
    """
    Deletes a node (except the tail) in a linked list given a pointer to that node.
    
    The function copies the data from the next node to the current node and then deletes the next node.
    
    Parameters:
    node (Node): The node to be deleted.
    
    Time Complexity: O(1) - The operation is done in constant time.
    Space Complexity: O(1) - No additional space is used.
    """
    if node is None or node.next is None:
        raise Exception("Cannot delete the last node or a null node")
    
    # Copy the data from the next node to the current node
    node.data = node.next.data
    # Bypass the next node
    node.next = node.next.next