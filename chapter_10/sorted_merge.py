import unittest

#Time Complexity: O(N) where n would be 'b'
def merged_sort(a, b):
    sorted(a)
    sorted(b)
    idx_b = 0
    idx_a = 0
    result = []
    while idx_b < len(b):
        if idx_a == len(a) or b[idx_b] < a[idx_a]:
            result.append(b[idx_b])
            idx_b += 1
        else:
            result.append(a[idx_a])
            idx_a += 1
    result = result + a[idx_a:] if idx_a < len(a) else result
    return result

class Test(unittest.TestCase):
    test_cases =  [
        ([1,3,4,5,7], [2,6], [1,2,3,4,5,6,7]),
        ([2, 4, 8, 10], [1, 3, 7, 21], [1, 2, 3, 4, 7, 8, 10, 21])
    ]

    functions = [merged_sort]
    def test_merged_sort(self):
        for function in self.functions:
            for a , b, expected in self.test_cases:
                result = function(a, b)
                assert result == expected

if __name__ == '__main__':
    unittest.main()