import unittest


def permutation_without_dups(letters):
    return permutations("", letters)

def permutations(partial, letters):
    if len(letters) == 0:
        return [partial]
    permutation = []
    for i, letter in enumerate(letters):
        letter_before = letters[:i]
        letter_after = letters[i+1:]
        next_letter = letter_before + letter_after
        permutation += permutations(partial + letter, next_letter)
    return permutation

class Test(unittest.TestCase):
  def test_permutations(self):
    self.assertEqual(permutation_without_dups("ABCD"), ["ABCD", "ABDC", "ACBD", "ACDB",
        "ADBC", "ADCB", "BACD", "BADC", "BCAD", "BCDA", "BDAC", "BDCA",
        "CABD", "CADB", "CBAD", "CBDA", "CDAB", "CDBA", "DABC", "DACB",
        "DBAC", "DBCA", "DCAB", "DCBA"])
    self.assertListEqual(permutation_without_dups("abc"),
                             ['abc', 'acb', 'bac', 'bca', 'cab', 'cba',])

if __name__ == "__main__":
  unittest.main()