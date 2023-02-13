import unittest

#O(j - i)
def bits_insertion(n, m, i, j):
    # do a liner search through the bits of M (from tail to head)
    # and if you find 1, do a bit insertion to N
    # if you find 0, clear idxth bit of N using a mask
    for index in range(j - i + 1):
        if (m >> index) & 1 != 0:
            # set bit
            n |= 1 << (index + i)
        else:
            # clear bit
            mask = ~(1 << (index + i))
            n &= mask
    return n


class TestCase(unittest.TestCase):
    test_cases = [
        ((int("10000000000", 2), int("10011", 2), 2, 6), int("10001001100", 2)),
        ((int("11111111111", 2), int("10011", 2), 2, 6), int("11111001111", 2)),
    ]

    functions = [bits_insertion]

    def test_insertion(self):
        for function in self.functions:
            for (n, m, i, j), expected in self.test_cases:
                result = function(n, m, i, j)
                error_msg = f"{function.__name__}: {result:b} != {expected:b}"
                assert result == expected, error_msg

if __name__ == "__main__":
    unittest.main()