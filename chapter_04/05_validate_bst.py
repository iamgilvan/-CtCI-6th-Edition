import unittest

from chapter_04.binary_search_tree import BinarySearchTree
from chapter_04.binary_tree import BinaryTree

# O(n) time
# O(h) space
def is_binary_search_tree(tree):
    return is_bst(tree.root)


def is_bst(node, min_val=None, max_val=None):
    if not node:
        return True
    #check if current node is not largest (left subtree)
    if min_val and node.key < min_val:
        return False

    #check if current node is not lowest  (right subtree)
    if max_val and node.key >= max_val:
        return False

    # check that the left subtree is a BST
    if is_bst(node.left, min_val, node.key) == False:
        return False

    # check that the right subtree is a BST
    if is_bst(node.right, node.key, max_val) == False:
        return False

    return True



class TestCase(unittest.TestCase):
    def test_is_binary_search_tree(self):
        bst = BinarySearchTree()
        bst.insert(20)
        bst.insert(9)
        bst.insert(25)
        bst.insert(5)
        bst.insert(12)
        bst.insert(11)
        bst.insert(14)

        t = BinaryTree()
        n1 = t.insert(5, None)
        n2 = t.insert(4, n1)
        n3 = t.insert(6, n1)
        n4 = t.insert(3, n2)
        t.insert(6, n2)
        t.insert(5, n3)
        t.insert(2, n4)

        isBst = is_binary_search_tree(t)
        assert not isBst
        isBst = is_binary_search_tree(bst)
        assert isBst

if __name__ == "__main__":
    unittest.main()