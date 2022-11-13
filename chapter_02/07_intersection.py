import time
import unittest
from chapter_02.linked_list import LinkedList

# O(N)
def intersection(ll_a, ll_b):
    headA, headB = ll_a.head, ll_b.head
    visited_Nodes = set()
    while headA:
        visited_Nodes.add(headA)
        headA = headA.next

    while headB:
        if headB in visited_Nodes:
            return headB.value
        headB = headB.next

    return None

class Test(unittest.TestCase):
    test_cases = (
        ([4,1], [5,6,1], [8,4,5], 8),
        ([1, 9, 1], [3, 2, 4], [2, 4], 2),
        ([2, 6, 4], [1, 5], [], None),
    )

    test_functions = [
        intersection
    ]

    def test_palindrome(self):
        # true check
        for function in self.test_functions:
            start = time.perf_counter()
            for _ in range(50):
                for list1, list2, shared_list, expected in self.test_cases:
                    shared = LinkedList(shared_list)
                    ll_1 = LinkedList(list1)
                    ll_2 = LinkedList(list2)
                    ll_1.tail.next = shared.head
                    ll_1.tail = shared.tail
                    ll_2.tail.next = shared.head
                    ll_2.tail = shared.tail
                    assert function(ll_1, ll_2) == expected

            duration = time.perf_counter() - start
            print(f"{function.__name__} {duration * 1000:.1f}ms")

if __name__ == "__main__":
    unittest.main()