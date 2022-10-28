import unittest
import time
from copy import deepcopy


# O (NxN)

def rotate_matrix_algo(matrix):
    """rotates a matrix 90 degrees clockwise"""
    new_matrix = deepcopy(matrix)
    for i, row in enumerate(matrix):
        curr_row = 0
        for j, number in enumerate(row):
            curr_column = len(row) - i - 1
            new_matrix[curr_row][curr_column] = number
            curr_row += 1
    return new_matrix

class Test(unittest.TestCase):
    test_cases = [
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            [
                [7, 4, 1],
                [8, 5, 2],
                [9, 6, 3],
            ]
        ),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]

    testable_functions = [
        rotate_matrix_algo
    ]

    def test_rotate_matrix(self):
        for function in self.testable_functions:
            start = time.perf_counter()
            for _ in range(1000):
                for matrix, expected in self.test_cases:
                    actual = function(matrix)
                    assert actual == expected, f"Failed {function.__name__} for: {[matrix]}"
            duration = time.perf_counter() - start
            print(f"{function.__name__} {duration * 1000:.1f}ms")

if __name__ == "__main__":
    unittest.main()