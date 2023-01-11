import unittest
from chapter_04.binary_search_tree import BinarySearchTree, Node

# O(h) - where h is the height of the tree.
def get_successor(node):
    if not node:
        return None

    current_node = node.right
    while current_node:
        if not current_node.left:
            break
        current_node = current_node.left

    return current_node.key if current_node else None

class TestCase(unittest.TestCase):
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)

    tests = [
        (9, 11),
        (20, 25),
        (5, None),
    ]

    def test_successor(self):
        for [key, result] in self.tests:
            node = self.bst.get_node(key)
            assert result == get_successor(node)

if __name__ == "__main__":
    unittest.main()