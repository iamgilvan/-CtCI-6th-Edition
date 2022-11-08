import time
import unittest
from chapter_02.linked_list import LinkedList


def partition(ll, x):
    current = ll.tail = ll.head

    while current:
        next_node = current.next
        current.next = None
        if current.value < x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = next_node

    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None
    values_processed = []
    node = ll.head
    while node:
        values_processed.append(node.value)
        node = node.next
    return values_processed


class Test(unittest.TestCase):

    test_functions = [
        partition,
    ]

    def test_partition(self):
        # true check
        for function in self.test_functions:
            start = time.perf_counter()
            for _ in range(100):
                #for values, expected in self.test_cases:
                ll = LinkedList.generate(10, 0, 99)
                values = function(ll , ll.head.value )
                key_index = values.index(ll.head.value)
                values_before_index = values[:key_index]
                values_after_index = values[key_index + 1:]
                for value in values_before_index:
                    if value > values[key_index]:
                        assert False
                for value in values_after_index:
                    if value < values[key_index]:
                        assert False
                assert True

            duration = time.perf_counter() - start
            print(f"{function.__name__} {duration * 1000:.1f}ms")

def example():

    ll = LinkedList.generate(10, 0, 99)
    print(ll.values())
    partition(ll, ll.head.value)
    print(ll.values())


if __name__ == "__main__":
    example()
    #unittest.main()