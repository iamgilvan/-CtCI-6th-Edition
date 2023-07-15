import unittest

# Time Complexity: O(logN)
# Binary Search
def searched_in_rotated_array(arr, target):
    start_idx, last_idx = 0, len(arr) - 1

    while start_idx <= last_idx:
        middle_idx = (start_idx + last_idx) // 2
        if arr[middle_idx] == target:
            return middle_idx
        if arr[start_idx] <= arr[middle_idx]:
            if target > arr[middle_idx]  or target < arr[start_idx]:
                start_idx = middle_idx + 1
            else:
                last_idx = middle_idx - 1
        else:
            if target < arr[middle_idx] or target > arr[last_idx]:
                last_idx = middle_idx - 1
            else:
                start_idx = middle_idx + 1

class Test(unittest.TestCase):
    test_cases = [
        ([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 5, 8),
        ([14, 15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10], 16, 2)
    ]
    functions = [searched_in_rotated_array]
    def test_group_anagram(self):
        for function in self.functions:
            for arr, target, expected in self.test_cases:
                result = function(arr, target)
                assert result == expected

if __name__ == '__main__':
    unittest.main()