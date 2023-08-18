import time
import unittest
from chapter_02.linked_list import LinkedList

# Time Compelxity: O(N), Space Complexity: O(1)
def sum_list(a, b):
    sum = 0
    ll_a = LinkedList()
    for v in a:
        ll_a.add_to_beginning(v)
    ll_b = LinkedList()
    for v in b:
        ll_b.add_to_beginning(v)

    node_a = ll_a.head
    node_b = ll_b.head
    a_str = ''
    b_str = ''
    while node_a:
        a_str += str(node_a.value)
        b_str += str(node_b.value)
        node_a = node_a.next
        node_b = node_b.next
    if a_str == '' or b_str == '':
        return []
    sum = int(a_str) + int(b_str)
    return_values = [int(v) for v in str(sum)]
    return_values.reverse()
    return return_values


class Test(unittest.TestCase):
    test_cases = (
        ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
        ([], [], []),
        ([3, 2, 1], [3, 2, 1], [6, 4, 2]),
    )

    test_functions = [
        sum_list,
    ]

    def test_partition(self):
        # true check
        for function in self.test_functions:
            start = time.perf_counter()
            for _ in range(10):
                for a, b, expected in self.test_cases:
                    reverse_list = function(a, b)
                    assert reverse_list == expected

            duration = time.perf_counter() - start
            print(f"{function.__name__} {duration * 1000:.1f}ms")

if __name__ == "__main__":
    unittest.main()