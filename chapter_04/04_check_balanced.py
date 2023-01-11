import unittest
from chapter_04.binary_search_tree import Node

# O(n)
def is_balanced(node):
    if node == None:
        return 0

    # checking left subtree
    leftSubtreeHeight = is_balanced (node.left);
    # if left subtree is not balanced then the entire tree is also not balanced
    if leftSubtreeHeight == -1:
        return -1

    # checking right subtree
    rightSubtreeHeight = is_balanced (node.right);
    #if right subtree is not balanced then the entire tree is also not balanced
    if rightSubtreeHeight == -1:
        return -1

    #checking the difference of left and right subtree for current node
    if abs(leftSubtreeHeight - rightSubtreeHeight) > 1:
       return -1

    #if it is balanced then return the height
    return max(leftSubtreeHeight, rightSubtreeHeight) + 1

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

    def test_check_balance(self):
        for [tree_gen, result] in self.tests:
            resultValue = is_balanced(tree_gen())
            isBalanced = True if resultValue > -1 else False
            assert result == isBalanced

if __name__ == "__main__":
    unittest.main()