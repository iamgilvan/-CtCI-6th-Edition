class Node:
    def __init__(self, key):
        self.key = key
        self.visited = False
        self.children = []

class Graph:
    def __init__(self):
        self.root = None

    def insert(self, key, parent):
        new_node = Node(key)
        if parent is None:
            if self.root is None:
               self.root = new_node
               return new_node
            raise Exception("A root already exists")
        parent.children.append(new_node)
        return parent

    def get_node(self, node, key):
        if node is None:
            return None
        node.visited = True
        if key in node.key:
            return node
        for child in node.children:
            if child.visited == False:
                if key in child.key:
                    return child
                self.get_node(child, key)