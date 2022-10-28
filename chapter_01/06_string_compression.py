import unittest
import time

# O (N)
def string_compression_algo(main_word: str) -> str:
    count = 0
    compressed = ''
    last_char = main_word[0] if len(main_word) > 0 else ''

    if last_char == '':
        return ''

    for char in main_word:
        if last_char != char:
            compressed += last_char + str(count)
            count = 1
            last_char = char
            continue
        count += 1
    compressed += last_char + str(count)
    return compressed

class Test(unittest.TestCase):
    test_cases = {
        ("aabcccccaaa"): "a2b1c5a3",
        ("abcdef"): "a1b1c1d1e1f1",
        ("aabb"): "a2b2",
        ("aaa"): "a3",
        ("a"): "a1",
        (""): "",
    }

    testable_functions = [
        string_compression_algo
    ]

    def test_string_compression(self):
        for function in self.testable_functions:
            start = time.perf_counter()
            for _ in range(1000):
                for word, expected in self.test_cases.items():
                    actual = function(word)
                    assert actual == expected, f"Failed {function.__name__} for: {[word]}"
            duration = time.perf_counter() - start
            print(f"{function.__name__} {duration * 1000:.1f}ms")

if __name__ == "__main__":
    unittest.main()