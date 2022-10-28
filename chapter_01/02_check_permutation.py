import unittest

# O (N)
def check_permutation_using_sorted(word1: str, word2: str) -> bool:
    word1, word2 = sorted(word1), sorted(word2)
    if len(word1) > len(word2):
        for i in range(0, len(word2)):
            if word1[i] != word2[i]:
                return False
        return True

    for i in range(0, len(word1)):
            if word1[i] != word2[i]:
                return False
    return True

class Test(unittest.TestCase):
    test_cases = [
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False)
        ]

    test_functions = [
        check_permutation_using_sorted
    ]

    def test_permutation(self):
        # true check
        for check_permutation in self.test_functions:
            for str1, str2, expected in self.test_cases:
                assert check_permutation(str1, str2) == expected

if __name__ == "__main__":
    unittest.main()