from collections import defaultdict
import unittest

#Time Complexity O(n)
def group_anagram_with_dict(arr):
    result = defaultdict(list)
    for word in arr:
        sorted_word = ''.join(sorted(word, key=str.lower))
        result[sorted_word].append(word)
    return result

#Time Complexity : O(nlogn)
def group_anagrams(input):
    tuple_array = [(sorted(word), word) for word in input]
    tuple_array.sort(key=lambda x: x[0])
    return [pair[1] for pair in tuple_array] #  (['cat', 'door', 'act', 'dog', 'odor'], 3) 

class Test(unittest.TestCase):
    test_cases = [
        (['aet', 'tea', 'tan', 'ate','nat','bat'], 3),
        (['cat', 'door', 'act', 'dog', 'odor'], 3)
    ]
    functions = [group_anagram_with_dict]
    def test_group_anagram(self):
        for function in self.functions:
            for groups, groups_number_expected in self.test_cases:
                result = function(groups)
                assert len(result) == groups_number_expected
if __name__ == '__main__':
    unittest.main()