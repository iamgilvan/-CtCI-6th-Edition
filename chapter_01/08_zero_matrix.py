import unittest
import time
from copy import deepcopy


# O (MXN)

def zero_matrix_algo(matrix):
    new_matrix = deepcopy(matrix)
    for index_row, row in enumerate(matrix):
        if 0 in matrix[index_row]:
            new_matrix[index_row] = [0] * len(row)
            count = 0
            zero_in_column = False
            idx_col = 0
            for j, number in enumerate(matrix[index_row]):
                if 0 == number:
                    zero_in_column = True
                    idx_col = j
                    break

            if zero_in_column:
                for i in range(len(row)):
                    new_matrix[count][idx_col] = 0
                    count += 1
    return new_matrix

class Test(unittest.TestCase):
    test_cases = [
        (
           [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        ),
    ]

    testable_functions = [
        zero_matrix_algo
    ]

    def test_zero_matrix(self):
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