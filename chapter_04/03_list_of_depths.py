from collections import deque
import unittest

from chapter_02.linked_list import LinkedList
from chapter_04.binary_search_tree import BinarySearchTree, Node
from chapter_04.binary_tree import BinaryTree

#(O)N
def create_node_list_by_depth(tree):
    if tree is None:
        return 0
    # store depths level of the tree
    levels = {}
    queue = deque()
    # add the first node and level as a tuple
    queue.append((tree, 0))

    while len(queue) > 0:
        # get node and level
        node, level = queue.popleft()
        if level not in levels: # check key in dictionary
            # First node in the level
            levels[level] = LinkedList()
        # Nodes already exist
        levels[level].add(node)

        # Push onto queue
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    return len(levels)

def get_tree(elements):
    if not elements:
        return None

    middleOfArr = len(elements) // 2
    # initialize a new node
    node = Node(elements[middleOfArr])
    # insert values to the left side of the tree
    node.left = get_tree(elements[:middleOfArr])
    # insert values to the right side of the tree
    node.right = get_tree(elements[middleOfArr+1:])
    return node

class TestCase(unittest.TestCase):
    tests = [
        ([3, 5, 7, 9, 10, 18, 20], 3),
        ([3, 5, 7, 9, 10, 18, 20, 30], 4),
        ([3, 5, 7, 9, 10, 18, 20, 30, 40], 4),
        ([], 0)
    ]

    def test_min_height(self):
        for [elements, height] in self.tests:
            tree = get_tree(elements)
            assert height == create_node_list_by_depth(tree)

if __name__ == "__main__":
    unittest.main()