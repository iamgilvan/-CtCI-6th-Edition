import unittest


class RankNode:
    def __init__(self, data):
        self.val = data
        self.right = None
        self.left = None
        self.left_size = 0

def insert(root, val):
    if root is None:
        return RankNode(val)
    # updating size of left subtree
    if val < root.val:
        root.left = insert(root.left, val)
        root.left_size += 1
    else:
        root.right = insert(root.right, val)
    return root

def get_rank(root, x):
    """Get rank of Node with value X """
    if root.val == x:
        return root.left_size
    elif x < root.val:
        if root.left is None:
            return -1
        else:
            return get_rank(root.left, x)
    else:
        if root.right is None:
            return -1
        else:
            right_size = get_rank(root.right, x)
            if right_size == -1:
                return -1
            else:
                return root.left_size + (1+ right_size)

class Test(unittest.TestCase):
    test_cases = [
        (4, 2),
        (5, 4),
    ]

    def test_rank_from_stream(self):
        self.root = None
        for i in [ 5, 1, 4, 4, 5, 9, 7, 13, 3 ]:
            self.root = insert(self.root, i)
        for target, expected in self.test_cases:
            rank = get_rank(self.root, target)
            assert rank == expected

if __name__ == '__main__':
    unittest.main()