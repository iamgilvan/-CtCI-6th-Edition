import unittest
import time
from copy import deepcopy

# O (N)
def string_rotation_algo(s1: str, s2: str) -> bool:
    s1 = sorted(s1);
    s2 = sorted(s2);
    return True if s1 == s2 else False

class Test(unittest.TestCase):
    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ]

    testable_functions = [
        string_rotation_algo
    ]

    def test_string_rotation(self):
        for function in self.testable_functions:
            start = time.perf_counter()
            for _ in range(1000):
                for s1, s2, expected in self.test_cases:
                    actual = function(s1,s2)
                    assert actual == expected, f"Failed {function.__name__} for: {s1} and {s2}"
            duration = time.perf_counter() - start
            print(f"{function.__name__} {duration * 1000:.1f}ms")

if __name__ == "__main__":
    unittest.main()