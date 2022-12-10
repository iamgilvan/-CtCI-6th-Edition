import unittest

from chapter_03.stack import Stack

#(O)N
class SortedStack(Stack):
    def __init__(self):
        super().__init__()
        self.temp_stack = Stack()

    def push(self, item):
        # descending order
        if super().is_empty() or item < super().peek():
            super().push(item)
        else:
            # ascending order
            while super().peek() is not None and item > super().peek():
                self.temp_stack.push(super().pop())
            super().push(item)
            # descending order again with the smallest value on the top
            while not self.temp_stack.is_empty():
                super().push(self.temp_stack.pop())


class Tests(unittest.TestCase):
    def test_push_mixed_values(self):
        queue = SortedStack()
        queue.push(3)
        queue.push(2)
        queue.push(5)
        queue.push(1)
        queue.push(4)
        assert queue.pop() == 1
        assert queue.pop() == 2
        assert queue.pop() == 3
        assert queue.pop() == 4
if __name__=='__main__':
    unittest.main()