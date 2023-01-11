import unittest

from chapter_04.binary_tree import BinaryTree

def first_common_ancestor_for_bst(tree, p, q):

    if  p.key < tree.key and q.key < tree.key:
        return first_common_ancestor(tree.left, p, q)

    if  p.key > tree.key and q.key > tree.key:
        return first_common_ancestor(tree.right, p, q)

    return tree

# O(N)
def first_common_ancestor(tree, p, q):

    def dfs(node):
        if not node:
            return False, None
        left, ans = dfs(node.left)
        right, ans = dfs(node.right)
        currentNode = node == p or node == q
        if (left and right) or (left and currentNode) or (currentNode and right):
            return True, node
        return left or right or currentNode, None
    result, node = dfs(tree.root)
    return node

class TestCase(unittest.TestCase):
    t = BinaryTree()
    n1 = t.insert(1, None)
    n2 = t.insert(2, n1)
    n3 = t.insert(3, n1)
    n4 = t.insert(4, n2)
    n5 = t.insert(5, n2)
    n7 = t.insert(7, n3)
    n8 = t.insert(8, n4)

    def test_first_common_ancestor(self):
        result = first_common_ancestor(self.t, self.n3, self.n4)
        assert self.n1 == result


if __name__=="__main__":
    unittest.main()