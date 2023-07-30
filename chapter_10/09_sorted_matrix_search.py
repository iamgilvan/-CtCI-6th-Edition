import unittest

def binary_search(arr, target):
    start_idx = 0
    last_idx = len(arr) - 1
    while start_idx <= last_idx:
        middle_idx = (start_idx + last_idx) // 2
        if arr[middle_idx] == target:
            return True
        elif arr[middle_idx] > target:
            last_idx = middle_idx - 1
        else:
            start_idx = middle_idx + 1
    return False

# This solution uses binary search
# #Time complexity : O(M*logN)
def sorted_matrix_search(matrix, target):
    for arr in matrix:
        result = binary_search(arr, target)
        if result:
            return True
    return False


'''
This solution compares matrix elements with target number by moving down and left.
#Time complexity : O(M*N)
'''
def sorted_matrix_search_by_moving(matrix, target):
    row = 0
    column = len(matrix[0]) - 1
    while row < len(matrix) and column >= 0:
        if target > matrix[row][column]:
            row += 1
        elif target < matrix[row][column]:
            column -= 1
        else: # found element
            return True
    return False

# def sorted_matrix_search_in_one_array(matrix, target):
#     full_arr = []
#     for arr in matrix:
#         full_arr.extend(arr)
#     return binary_search(sorted(full_arr), target)

class Test(unittest.TestCase):
    matrix = [
        [1,  2,  3,  4,  5,  6,  7,  8,  9],
        [5,  10, 15, 20, 25, 30, 35, 40, 45],
        [10, 20, 30, 40, 50, 60, 70, 80, 90],
        [13, 23, 33, 43, 53, 63, 73, 83, 93],
        [14, 24, 34, 44, 54, 64, 74, 84, 94],
        [15, 25, 35, 45, 55, 65, 75, 85, 95],
        [16, 26, 36, 46, 56, 66, 77, 88, 99]
    ]
    test_cases = [
        (3, True),
        (73, True),
        (-1, False),
        (150, False),
    ]
    functions = [sorted_matrix_search, sorted_matrix_search_by_moving]
    def test_sorted_matrix_search(self):
        for function in self.functions:
            for target, expected in self.test_cases:
                result = function(self.matrix, target)
                assert result == expected

if __name__ == '__main__':
    unittest.main()