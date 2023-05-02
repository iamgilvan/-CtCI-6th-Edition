import unittest

# O(3^n)
def count_ways(n):
    if n < 0:
        return 0;
    elif n == 0:
        return 1;
    else:
        return count_ways(n - 1) + count_ways(n - 2) + count_ways(n - 3)

class Test(unittest.TestCase):
  def test_triple_step(self):
    self.assertEqual(count_ways(3), 4)
    self.assertEqual(count_ways(7), 44)
    self.assertEqual(count_ways(4), 7)

if __name__ == "__main__":
    unittest.main()