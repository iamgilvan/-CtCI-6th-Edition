import unittest

def pairwise_swap(number) -> int:
     return ((number & 0x55555555) << 1) | ((number & 0xAAAAAAAA) >> 1)

class Test(unittest.TestCase):
    test_cases = [
        (123, 183),
        (781, 782),
        (278, 553)
    ]

    functions = [pairwise_swap]

    def test_pairwise_swap(self):
        for function in self.functions:
            for number ,expected in self.test_cases:
                result = function(number)
                assert result == expected

if __name__ == "__main__":
    print(0x55555555)
    print(0xaaaaaaaa)
    unittest.main()