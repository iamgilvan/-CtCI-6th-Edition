import unittest

# Time Complexity: O(N* N!), Space Complexity: O(N*N!)
def permutation_with_dups(letters):
    return permutations("", sorted(letters))

def permutations(partial, letters):
    if len(letters) == 0:
        return [partial]
    permutation = []
    previous_letter = None
    for i, letter in enumerate(letters):
        if letter == previous_letter:
            continue
        next_partial = partial + letter
        letter_before = letters[:i]
        letter_after = letters[i+1:]
        next_letter = letter_before + letter_after
        permutation += permutations(next_partial, next_letter)
        previous_letter = letter
    return permutation

class Test(unittest.TestCase):
  def test_permutations(self):
    self.assertEqual(permutation_with_dups("abca"), ["aabc", "aacb", "abac", "abca",
        "acab", "acba", "baac", "baca", "bcaa", "caab", "caba", "cbaa"])
    self.assertEqual(permutation_with_dups("ABCD"), ["ABCD", "ABDC", "ACBD", "ACDB",
        "ADBC", "ADCB", "BACD", "BADC", "BCAD", "BCDA", "BDAC", "BDCA",
        "CABD", "CADB", "CBAD", "CBDA", "CDAB", "CDBA", "DABC", "DACB",
        "DBAC", "DBCA", "DCAB", "DCBA"])
    self.assertListEqual(permutation_with_dups("aab"), ['aab', 'aba', 'baa'])

if __name__ == "__main__":
  unittest.main()