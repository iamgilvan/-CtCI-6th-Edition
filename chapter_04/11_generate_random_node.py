import random
import unittest

from chapter_04.binary_search_tree import BinarySearchTree
#O(h) where h is the height of tree.
def get_random_node(tree):
    current_node = tree.root

    directions = ['self', 'right', 'left']
    weights = [1,1,1]
    while current_node:
        # get direction
        direction = random.choices(directions, weights)[0]
        if direction == 'self':
            return current_node.key
        if direction == 'right':
            if not current_node.right:
                return current_node.key
            current_node = current_node.right
        else:
            if not current_node.left:
                return current_node.key
            current_node = current_node.left

class TestCase(unittest.TestCase):
    bst = BinarySearchTree()
    bst.insert(11)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(6)
    bst.insert(14)
    bst.insert(20)

    def test_generate_random_node(self):
        key = get_random_node(self.bst)
        print(key)
        assert True

    def test_delete_node(self):
        tree = BinarySearchTree().delete_node(self.bst.root, 12)
        assert tree.right.left.key == 14

if __name__ == '__main__':
    unittest.main()