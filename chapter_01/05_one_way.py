import unittest

def one_way_pythonic(main_word: str, edited_work: str) -> bool:
    diff = set(list(main_word)) - set(list(edited_work))
    return False if len(diff) > 1 else True

# O (N)
def one_way_algo(main_word: str, edited_work: str) -> bool:
    count = 0

    for char in main_word:
        if char not in edited_work:
            count += 1
            if count > 1:
                return False
    return True

class Test(unittest.TestCase):
    test_cases = {
        ("pale", "ple"): True,
        ("pales", "pale"): True,
        ("pale", "bale"): True,
        ("pale", "bake"): False,
    }

    testable_functions = [
        one_way_algo, one_way_pythonic
    ]

    def test_one_way(self):
        for functions in self.testable_functions:
            for args, expected in self.test_cases.items():
                actual = functions(*args)
                assert actual == expected, f"Failed {functions.__name__} for: {[*args]}"

if __name__ == "__main__":
    unittest.main()