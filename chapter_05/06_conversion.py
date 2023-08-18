import unittest

# Time Complexity: O(b), Space Complexity: O(1)
def bit_swap_required(numberFrom: int, numberTo: int) -> int:
    count = 0
    number = numberFrom ^ numberTo # XOR operator
    while number != 0:
        count += number & 1
        number >>= 1
    return count

class Test(unittest.TestCase):
    test_cases = [
        #  29       15
        (0b11101, 0b01111 , 2),
    ]

    functions = [bit_swap_required]

    def test_bit_swap_required(self):
        for function in self.functions:
            for numberFrom, numberTo ,expected in self.test_cases:
                result = function(numberFrom, numberTo)
                assert result == expected
if __name__ == "__main__":
    unittest.main()