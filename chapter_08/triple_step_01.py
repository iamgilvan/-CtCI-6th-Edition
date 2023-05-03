import unittest

# O(3^n)
def count_ways(n):
    if n < 0:
        return 0;
    elif n == 0:
        return 1;
    else:
        return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)


def count_way_to_step(number):
    if number < 1:
        return None
    else:
        return __count_way_to_step(number, {})

def __count_way_to_step(number, table):
    if number == 0:
        return 1
    elif number < 0:
        return 0
    if number not in table:
        table[number] = __count_way_to_step(number-3, table) + __count_way_to_step(number-2, table) + __count_way_to_step(number-1, table)
    return table[number]


class Test(unittest.TestCase):
  def test_triple_step(self):
    self.assertEqual(count_ways(3), 4)
    self.assertEqual(count_ways(7), 44)
    self.assertEqual(count_ways(4), 7)
    self.assertEqual(count_way_to_step(4), 7)

if __name__ == "__main__":
    unittest.main()