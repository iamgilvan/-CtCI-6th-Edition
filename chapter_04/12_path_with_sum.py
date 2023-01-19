import unittest
from binary_tree import BinaryTree

#O(N)
def count_path_with_sum(node, sum):
    if not node:
        return 0
    # count paths with sum starting from root
    pathFromRoot = count_path_with_sum_from_node(node, sum, 0)
    # find paths from left sub tree and right sub tree
    pathOnLeft = count_path_with_sum(node.left, sum)
    pathOnRight = count_path_with_sum(node.right, sum)

    return pathFromRoot + pathOnLeft + pathOnRight


def count_path_with_sum_from_node(node, sum, currentSum):
    # If node is null, no path exists
    if not node:
        return 0
    # Update the current sum
    currentSum += node.key
    totalPath = 0
    # If current sum and target sum matches, we found a path
    if currentSum == sum:
        totalPath += 1

    # Find paths for left subtree and right subtree
    totalPath += count_path_with_sum_from_node(node.left, sum, currentSum)
    totalPath += count_path_with_sum_from_node(node.right, sum, currentSum)

    return totalPath

class TestCase(unittest.TestCase):
    t1 = BinaryTree()
    n1 = t1.insert(10, None)
    n2 = t1.insert(5, n1)
    n3 = t1.insert(-3, n1)
    n4 = t1.insert(3, n2)
    n5 = t1.insert(2, n2)
    n6 = t1.insert(3, n4)
    n7 = t1.insert(-2, n4)
    n8 = t1.insert(1, n5)
    n9 = t1.insert(11, n3)
    n10 = t1.insert(8, n9)
    n11 = t1.insert(-8, n10)

    def test_count_path_with_sum(self):
        assert 5 == count_path_with_sum(self.t1.root, 8)
        assert 2 == count_path_with_sum(self.t1.root, 6)

if __name__ == '__main__':
    unittest.main()