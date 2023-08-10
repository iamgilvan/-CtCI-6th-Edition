
import unittest

#Time Complexity : O(n log n)
#Space Complexity : O(1)

def peaks_and_valley(arr):
    arr.sort()
    for i in range(1, len(arr), 2):
        temp = arr[i - 1]
        arr[i - 1] = arr[i]
        arr[i] = temp
    return arr

class Test(unittest.TestCase):
    test_cases = [
        ([5, 3, 1, 2, 3], [2, 1, 3, 3, 5])
    ]
    functions = [peaks_and_valley]
    def test_peak_and_valley(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()