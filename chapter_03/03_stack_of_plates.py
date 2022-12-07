import unittest

from chapter_03.stack import Stack


class SetOfStacks:
    def __init__(self, capacity):
        super().__init__()
        self.capacity = capacity
        self.stacks = []

    def get_last_stack(self):
        if not self.stacks:
            return None
        return self.stacks[-1]

    def is_empty(self):
        last = self.get_last_stack()
        return not last or len(last) == self.capacity

    def push(self, v):
        last = self.get_last_stack()
        if last and not len(last) == self.capacity:
            last.push(v)
        else:
            stack = Stack()
            stack.push(v)
            self.stacks.append(stack)

    def pop(self):
        last = self.get_last_stack()
        if not last:
            return None
        v = last.pop()
        if len(last) == 0:
            del self.stacks[-1]
        return v

    def pop_at(self, index):
        return self.left_shift(index, True)

    def left_shift(self, index, remove_top):
        stack = self.stacks[index]
        removed_item = stack.pop() if remove_top else stack.remove_bottom()
        if len(stack) == 0:
            del self.stacks[index]
        elif len(self.stacks) > index + 1:
            v = self.left_shift(index + 1, False)
            stack.push(v)
        return removed_item


class Tests(unittest.TestCase):
    def test_stacks(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(35):
            lst.append(stacks.pop())
        assert lst == list(reversed(range(35)))

    def test_pop_at(self):
        stacks = SetOfStacks(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(31):
            lst.append(stacks.pop_at(0))
        assert lst == list(range(4, 35))


if __name__ == "__main__":
    unittest.main()
