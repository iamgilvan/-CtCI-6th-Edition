import time
import unittest

from chapter_02.linked_list import LinkedList

# O(N) space
def delete_middle_node(ll, value_to_remove):
    current = ll.head

    while current:
        if current.value == value_to_remove:
            current.value = current.next.value
            current.next = current.next.next
            return ll
        current = current.next
    return ll

class Test(unittest.TestCase):
    test_cases = (
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [1, 2, 3, 4, 6, 7, 8, 9]),
        ([1, 3, 4, 5, 6, 7, 8, 9], 2, [1, 3, 4, 5, 6, 7, 8, 9]),
    )

    test_functions = [
        delete_middle_node
    ]

    def test_delete_middle_node(self):
        # true check
        for function in self.test_functions:
            start = time.perf_counter()
            for _ in range(100):
                for values, value_to_remove, expected in self.test_cases:
                    expected = expected.copy()
                    deduped = function(LinkedList(values), value_to_remove)
                    assert deduped.values() == expected

            duration = time.perf_counter() - start
            print(f"{function.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()