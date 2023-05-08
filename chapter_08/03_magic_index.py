import unittest

def magic_fast(arr):
    return __magic_fast(arr, 0, len(arr) - 1)

def __magic_fast(arr, start, end):
    if end < start:
        return -1
    middle = (start + end) // 2
    if middle == arr[middle]:
        return middle
    elif arr[middle] > middle:
        return __magic_fast(arr,start, middle-1)
    else:
        return __magic_fast(arr,middle + 1, end)
class TestCase(unittest.TestCase):
    my_array = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
    array_distinct = [-1, 0, 1, 2, 3, 5]
    def test_magic_index(self):
        self.assertEqual(magic_fast(self.my_array), 7)
        self.assertEqual(magic_fast(self.array_distinct), 5)
if __name__ == "__main__":
    unittest.main()