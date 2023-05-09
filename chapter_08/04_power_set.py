import unittest


def get_sub_set(numbers):
    ps = {frozenset()}
    for element in numbers:
        additions = set()
        for subset in ps:
            partial = subset.union(element)
            additions.add(partial)
        ps = ps.union(additions)

    print([list(x) for x in ps])
    return ps

class Test(unittest.TestCase):
    s = {'a', 'b', 'c'}
    def test_power_set(self):
        ps = get_sub_set(self.s)
        self.assertEqual(len(ps), 8)

if __name__ == "__main__":
    unittest.main()