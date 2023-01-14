from typing import List
import unittest

from binary_search_tree import BinarySearchTree
def bst_sequences(root: BinarySearchTree):

    def __visit(roots: List):
            output = []
            for root in roots:
                choices = [choice for choice in roots if choice != root]
                if root.left:
                    choices.append(root.left)
                if root.right:
                    choices.append(root.right)

                if len(choices) > 0:
                    sequences = __visit(choices)
                    for sequence in sequences:
                        output.append([root.key] + sequence)
                else:
                    output.append([root.key])
            return output

    return __visit([root.root])

class TestCase(unittest.TestCase):
    @staticmethod
    def create_tree() -> BinarySearchTree:
        bst = BinarySearchTree()
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        return bst

    def test_bst_sequences(self):
        root = TestCase.create_tree()
        sequences = bst_sequences(root)
        actual_result  = set(tuple(sequence) for sequence in sequences)
        expected_result = set(tuple(item) for item in [[2, 1, 3],[2, 3, 1]])
        self.assertSetEqual(actual_result, expected_result)

if __name__ =="__main__":
    unittest.main()