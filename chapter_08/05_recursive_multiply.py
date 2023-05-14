'''Method 1
Simple way to multiply using addition
Time Complexity : O(N)
'''
import unittest


def multiply_without_operation(number1, number2):
    result = 0
    bigger = number1 if number1 > number2 else number2
    smaller = number1 if number1 < number2 else number1
    for _ in range(smaller):
        result += bigger
    return result


'''Method 2
This solution uses recursive function with addition, substraction
'''
def recursive_multiply(number1, number2):
    if number1 == 0 or number2 == 0:
        return 0;

    if number1 == 1:
        return number2

    return recursive_multiply(number1 - 1, number2) + number2

class Test(unittest.TestCase):
    def test_multiply_without_operation(self):
        self.assertEqual(multiply_without_operation(7, 9), 63)

    def test_recursive_multiply(self):
        self.assertEqual(recursive_multiply(2, 3), 6)
        self.assertEqual(recursive_multiply(4, 5), 20)

if __name__ == "__main__":
    unittest.main()