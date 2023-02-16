
import unittest

#O(log n)
class NextNumber:
    def __init__(self, smallest, greatest):
        self.smallest = smallest
        self.greatest = greatest

def next_number(number):
    smallest = get_previous(number)
    greatest = get_next(number)
    return NextNumber(smallest, greatest)

def get_previous(number) -> int:
    number_of_zeros, number_of_ones = 0, 0
    temp = number

    while ((temp & 1) == 1):
        number_of_ones = number_of_ones + 1
        temp = temp >> 1

    if (temp == 0):
        return -1

    while (((temp & 1) == 0) and (temp != 0)):
        number_of_zeros = number_of_zeros + 1
        temp = temp >> 1

    return number - (1 << number_of_ones) - (1 << number_of_zeros - 1) + 1

def get_next(number) -> int:
    number_of_zeros, number_of_ones = 0, 0
    temp = number

    while (((temp & 1) == 0) and (temp != 0)):
        number_of_zeros += 1
        temp >>= 1

    while ((temp & 1) == 1):
        number_of_ones += 1
        temp >>= 1

    # If there is no bigger number with
    # the same no. of 1's
    if (number_of_zeros + number_of_ones == 31 or number_of_zeros + number_of_ones == 0):
        return -1

    return number + (1 << number_of_zeros) + (1 << number_of_ones - 1) - 1

class TestCase(unittest.TestCase):
    test_cases = [
        (5, 6, 3),
        (11, 13, 7),
    ]

    def test_flip_bit_to_bit(self):
        for number, greater, smaller in self.test_cases:
            result = next_number(number)
            assert result.greatest == greater
            assert result.smallest == smaller
if __name__ == "__main__":
    unittest.main()