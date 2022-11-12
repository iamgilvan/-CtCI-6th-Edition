import time
import unittest

from chapter_02.linked_list import LinkedList

#O(N)
def is_palindrome(value) -> bool:
    ll = LinkedList(value)
    ll_reverse = LinkedList()
    for v in value:
        ll_reverse.add_to_beginning(v)

    node = ll.head
    node_reverse = ll_reverse.head
    while node and node_reverse:
        if node.value != node_reverse.value:
            return False
        node = node.next
        node_reverse = node_reverse.next

    return True

class Test(unittest.TestCase):
    test_cases = (
        ([1, 2, 3, 4, 3, 2, 1], True),
        ([1], True),
        (["a", "a"], True),
        ("aba", True),
        ([], True),
        ([1, 2, 3, 4, 5], False),
        ([1, 2], False),
    )

    test_functions = [
        is_palindrome
    ]

    def test_palindrome(self):
        # true check
        for function in self.test_functions:
            start = time.perf_counter()
            for _ in range(50):
                for values, expected in self.test_cases:
                    assert function(values) == expected

            duration = time.perf_counter() - start
            print(f"{function.__name__} {duration * 1000:.1f}ms")

if __name__ == "__main__":
    unittest.main()