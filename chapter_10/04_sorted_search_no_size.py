import unittest

class Listy:
    def __init__(self, array):
        self.array = array

    def __getitem__(self, index):
        if index < len(self.array):
            return self.array[index]
        else:
            return -1

# Time Complexity: O(logN), Space Complexity: O(1)
def sorted_search_no_size(arr, target):
    last_index = 1
    while last_index < len(arr) and arr[last_index] < target:
        last_index *= 2

    start_index = 0
    while start_index <= last_index:
        middle_index = (start_index + last_index) // 2
        try:
            if arr[middle_index] == target:
                return middle_index
            elif arr[middle_index] > target:
                last_index = middle_index - 1
            else:
                start_index = middle_index + 1
        except IndexError:
            last_index = middle_index - 1
    return -1


class Test(unittest.TestCase):
    test_cases = [
        (Listy([1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25]), 5, 3),
        (Listy([1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25]), 19, 9),
        (Listy([1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25]), 30, -1)
    ]
    functions = [sorted_search_no_size]
    def test_sorted_search_no_size(self):
        for function in self.functions:
            for arr, target, expected in self.test_cases:
                result = function(arr.array, target)
                assert result == expected

if __name__ == '__main__':
    unittest.main()