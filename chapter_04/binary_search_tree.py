class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        # check if a new node
        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while current_node:
            # check existing key
            if current_node.key == key:
                return
            # iterate over left side
            if key < current_node.key:
                if current_node.left is None:
                    current_node.left = new_node
                    new_node.parent = current_node
                    return
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    new_node.parent = current_node
                    return
                current_node = current_node.right

    def get_node(self, key):
        current_node = self.root
        while current_node:
            if key == current_node.key:
                return current_node

            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        raise Exception("Can not find value in the tree")