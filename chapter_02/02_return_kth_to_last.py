
# O(N) space
import unittest
from chapter_02.linked_list import LinkedList


def kth_to_last(ll, k):
    leader = follower = ll.head
    count = 0

    while leader:
        if count >= k:
            follower = follower.next
        count += 1
        leader = leader.next
    return follower

class Test(unittest.TestCase):
    test_cases = (
        # list, k, expected
        ((10, 20, 30, 40, 50), 1, 50),
        ((10, 20, 30, 40, 50), 5, 10),
    )

    test_functions = [
        kth_to_last,
    ]

    def test_kth_to_last(self):
        # true check
        for linked_list_values, k, expected in self.test_cases:
            ll = LinkedList(linked_list_values)
            assert kth_to_last(ll, k).value == expected


if __name__ == "__main__":
    unittest.main()