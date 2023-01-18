import unittest

from binary_tree import BinaryTree

def is_subtree(tree, subtree):
    if not tree and not subtree:
        return True

    if not tree or not subtree:
        return False

    return same_tree(tree.root, subtree.root)
#O(N)
def same_tree(node, subnode):

    if not node or not subnode:
        return node == None and subnode == None

    if node.key == subnode.key:
        return same_tree(node.left, subnode.left) and same_tree(node.right, subnode.right)

    left = same_tree(node.left, subnode)
    right = same_tree(node.right, subnode)

    return left or right
class TestCase(unittest.TestCase):
    t1 = BinaryTree()
    n1 = t1.insert(1, None)
    n2 = t1.insert(2, n1)
    n3 = t1.insert(3, n1)
    n4 = t1.insert(4, n2)
    n5 = t1.insert(5, n2)
    n7 = t1.insert(7, n3)
    n8 = t1.insert(8, n4)

    t2 = BinaryTree()
    n40 = t2.insert(4, None)
    n80 = t2.insert(8, n40)

    def test_check_sub_tree(self):
        result = is_subtree(self.t1, self.t2)
        assert result

if __name__ == "__main__":
    unittest.main()