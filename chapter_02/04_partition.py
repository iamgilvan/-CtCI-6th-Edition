import time
import unittest
from chapter_02.linked_list import LinkedList


def partition(ll):
    current = ll.head
    values_processed = []
    while current:
       values_processed.append(current.value)
       current = current.next

    values_processed = sorted(values_processed)

    new_linkedList = LinkedList(values_processed)

    return new_linkedList.values()


class Test(unittest.TestCase):

    test_functions = [
        partition,
    ]

    def test_partition(self):
        # true check
        for function in self.test_functions:
            start = time.perf_counter()
            for _ in range(100):
                ll = LinkedList.generate(10, 0, 99)
                values = function(ll)
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

if __name__ == "__main__":
    unittest.main()