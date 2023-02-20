import unittest

def toBinary(number):
    # Check if the number is Between 0 to 1 or Not
    if number >= 1 or number <= 0:
        return "ERROR"
    # frac = 0.5
    answer = "0."
    # Setting a limit on length: 32 characters.
    while(number > 0):
        # Setting a limit on length: 32 characters
        if(len(answer) >= 32):
            return "ERROR"
        # Multiply number by 2 to check it 1 or 0
        b = number * 2
        if (b >= 1):
            answer = answer + "1"
            number = b - 1
        else:
            answer = answer + "0"
            number = b
    return answer

class TestCase(unittest.TestCase):
    test_cases = [
        (0.625, "0.101"),
        (0.72, "ERROR"),
    ]

    functions = [toBinary]

    def test_insertion(self):
        for function in self.functions:
            for number, expected in self.test_cases:
                result = function(number)
                assert result == expected

if __name__ == "__main__":
    unittest.main()