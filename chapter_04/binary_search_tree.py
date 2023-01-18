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

    #O(logN)
    def delete_node(self, node, key):
        if not node:
            return None

        if key > node.key:
            node.right = self.delete_node(node.right, key)
        elif key < node.key:
            node.left = self.delete_node(node.left, key)
        else:
            if not node.left and not node.right:
                node = None
            elif node.right:
                node.key = self.successor(node)
                node.right = self.delete_node(node.right, node.key)
            else:
                node.key = node.parent.key
                node.left = self.delete_node(node.left, node.key)
        return node

    def successor(self, node):
        curr_node = node.right
        while curr_node.left:
            curr_node = curr_node.left
        return curr_node.key