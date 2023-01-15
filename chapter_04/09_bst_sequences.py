from typing import List
import unittest

from binary_search_tree import BinarySearchTree
def bst_sequences(root: BinarySearchTree):

    def __visit(nodes: List):
            output = []
            # iterate over subtree
            for node in nodes:
                # get nodes left
                # remove one of the roots (valid choices), add its children to the set of choices
                choices = [choice for choice in nodes if choice != node]
                # adding children nodes to the list
                if node.left:
                    choices.append(node.left)
                if node.right:
                    choices.append(node.right)
                # check if there are any node 
                if len(choices) > 0:
                    # getting sequences
                    # recursively find all possible solutions for the new set of choices
                    sequences = __visit(choices)
                    # Iterate over sequences
                    for sequence in sequences:
                        # Adding current node/key to the sequence list
                        output.append([node.key] + sequence)
                else:
                    output.append([node.key])
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