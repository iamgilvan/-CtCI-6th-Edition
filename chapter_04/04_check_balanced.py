import unittest
from chapter_04.binary_search_tree import Node

class Height:
    def __init__(self):
        self.height = 0

# O(n)
def is_balanced(node, height):
    left_height = Height()
    right_height = Height()

    if node == None:
        return True

    left = is_balanced(node.left, left_height)
    right = is_balanced(node.right, right_height)

    height.height = max(left_height.height, right_height.height) + 1

    if abs(left_height.height - right_height.height) <= 1:
        return left and right

    return False

def _gen_balanced_1():
    root = Node(1)
    root.left = Node(2)
    return root


def _gen_balanced_2():
    root = Node(7)
    root.left = Node(2)
    root.left.left = Node(4)
    root.right = Node(3)
    root.right.left = Node(8)
    root.right.right = Node(9)
    root.right.right.right = Node(10)
    return root


def _gen_unbalanced_1():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)
    root.right = Node(3)
    root.right.left = Node(8)
    root.right.right = Node(9)
    root.right.right.right = Node(10)
    root.right.right.right.right = Node(11)
    return root


def _gen_unbalanced_2():
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(9)
    tree.right.left = Node(10)
    tree.left.left = Node(3)
    tree.left.right = Node(7)
    tree.left.right.right = Node(5)
    tree.left.left.left = Node(6)
    tree.left.right.left = Node(12)
    tree.left.right.left.left = Node(16)
    tree.left.right.left.right = Node(0)
    return tree

class TestCase(unittest.TestCase):
    tests = [
        (_gen_balanced_1, True),
        (_gen_balanced_2, True),
        (_gen_unbalanced_1, False),
        (_gen_unbalanced_2, False),
    ]

    def test_min_height(self):
        for [tree_gen, result] in self.tests:
            assert result == is_balanced(tree_gen(), Height())

if __name__ == "__main__":
    unittest.main()