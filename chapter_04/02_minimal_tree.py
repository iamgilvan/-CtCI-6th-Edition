import unittest
from chapter_04.binary_search_tree import Node

# O(n)
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


def get_binary_tree_height(node):
    if node == None:
        return 0
    leftHeight = get_binary_tree_height(node.left)
    rightHeight = get_binary_tree_height(node.right)
    return max(leftHeight, rightHeight) + 1


class TestCase(unittest.TestCase):
    tests = [
        ([3, 5, 7, 9, 10, 18, 20], 2),
        ([3, 5, 7, 9, 10, 18, 20, 30], 3),
        ([3, 5, 7, 9, 10, 18, 20, 30, 40], 3)
    ]

    def test_min_height(self):
        for [elements, height] in self.tests:
            tree = get_tree(elements)
            assert height == get_binary_tree_height(tree) - 1

if __name__ == "__main__":
    unittest.main()