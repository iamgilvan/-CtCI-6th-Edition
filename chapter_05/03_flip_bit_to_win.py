from ctypes import sizeof
import unittest

#O(log2n)
def flip_bit_to_win(number):
    currentLength, previousLength, maxLength = 0, 0, 0
    while number > 0:
        # If Current bit is a 1 then increment currLen++
        if ((number & 1) == 1):
            currentLength += 1
        # If Current bit is a 0 then check next bit of a
        elif ((number & 1) == 0):
            previousLength = 0 if ((number & 2) == 0) else currentLength;
            currentLength = 0

        maxLength = max(currentLength + previousLength, maxLength)
        number >>= 1

    return maxLength + 1

class TestCase(unittest.TestCase):
    test_cases = [
        (13, 4),
        (1775, 8),
        (15, 5)
    ]
    functions = [flip_bit_to_win]

    def test_flip_bit_to_bit(self):
        for function in self.functions:
            for number, expected in self.test_cases:
                result = function(number)
                assert result == expected
if __name__ == "__main__":
    unittest.main()