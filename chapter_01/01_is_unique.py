from collections import defaultdict
import time
from typing import List
import random
import unittest

def is_unique_char_using_dict(word: str) -> bool:
    dict = {}
    for char in word:
        if char in dict:
            return False
        dict[char] = 1
    return True

#O (N log N)
def is_unique_char_using_sorted(word: str) -> bool:
    word = sorted(word)
    previous_word = ''
    for char in word:
        if char == previous_word:
            return False
        previous_word = char
    return True

def is_unique_char_using_set(word: str) -> bool:
    chars = set()
    for char in word:
        if char in chars:
            return False
        chars.add(char)
    return True

def is_unique_chars_pythonic(word: str) -> bool:
    return len(set(word)) == len(word)

class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("44", False),
        ("117", False),
        ("132", True)]

    test_functions = [
        is_unique_char_using_dict,
        is_unique_char_using_sorted,
        is_unique_char_using_set,
        is_unique_chars_pythonic
    ]
    
    def test_is_unique_chars(self):
        num_runs = 10
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for is_unique_chars in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        is_unique_chars(text) == expected
                    ), f"{is_unique_chars.__name__} failed for value: {text}"
                    function_runtimes[is_unique_chars.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")

if __name__ == "__main__":
    unittest.main()