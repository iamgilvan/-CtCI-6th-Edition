import unittest


def find_all_duplicates(arr):
    my_arr = {}
    duplicates = []
    for i in arr:
        if i not in my_arr.keys():
            my_arr[i] = 1
        else:
            duplicates.append(i)
    return duplicates

def gat_all_duplicates(arr):
    four_kb_bits = 8*4*(2**10) # this is greater than 32000
    bit_vector = 1<<four_kb_bits
    duplicates = []
    for n in arr:
        check = bit_vector & 1<<n
        if check:
            duplicates.append(n)
        else:
            bit_vector = bit_vector | 1<<n
    return duplicates


class Test(unittest.TestCase):
    test_cases = [
        ([0,1,2,3,3,4,5,6,7,8,9,10,12,12], [3, 12])
    ]
    functions = [find_all_duplicates, gat_all_duplicates]
    def test_find_duplicates(self):
        for function in self.functions:
            for arr, expected in self.test_cases:
                result = function(arr)
                assert result == expected

if __name__ == '__main__':
    unittest.main()