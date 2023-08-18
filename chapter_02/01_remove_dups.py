import time
import unittest

from chapter_02.linked_list import LinkedList
# Time Complexity: O(N), Space Complexity: O(1)
def remove_dups(ll):
    current = ll.head
    previous = None
    seen = set()

    while current:
        if current.value in seen:
            previous.next = current.next
        else:
            seen.add(current.value)
            previous = current
        current = current.next
    ll.tail = previous
    return ll

# Time Complexity: O(N^2), Space Complexity: O(1)
def remove_dups_followup(ll):
    runner = current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    ll.tail = runner
    return ll


class Test(unittest.TestCase):
    test_cases = (
        ([], []),
        ([1, 1, 1, 1, 1, 1], [1]),
        ([1, 2, 3, 2], [1, 2, 3]),
        ([1, 2, 2, 3], [1, 2, 3]),
        ([1, 1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 3]),
    )

    test_functions = [
        remove_dups,remove_dups_followup
    ]

    def test_remove_dupes(self):
        # true check
        for function in self.test_functions:
            start = time.perf_counter()
            for _ in range(100):
                for values, expected in self.test_cases:
                    expected = expected.copy()
                    deduped = function(LinkedList(values))
                    assert deduped.values() == expected

                    deduped.add(5)
                    expected.append(5)
                    assert deduped.values() == expected

            duration = time.perf_counter() - start
            print(f"{function.__name__} {duration * 1000:.1f}ms")


if __name__ == "__main__":
    unittest.main()