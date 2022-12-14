class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, parent):
        new_node = Node(key)
        if parent is None:
            if self.root is not None:
                raise Exception("A root already exists")
            self.root = new_node
            return new_node

        if not parent.left:
            parent.left = new_node
            new_node.parent = parent
        elif not parent.right:
            parent.right = new_node
            new_node.parent = parent
        else:
            raise Exception("A node cannot have more than two children")
        return new_node

    def get_node(self, key):

        current_node = self.root
        while current_node:
            if current_node.key == key:
                return current_node

            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        raise Exception("Can not find value in the tree")