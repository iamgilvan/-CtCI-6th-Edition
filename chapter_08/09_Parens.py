
import unittest
'''Method 1
It adds a parenthes to front and back of subset and wraps the subset through a parenthes.
Also, duplicates can be eliminated by hashtable
'''
def get_parens(number):
    result = {}
    __get_parens(number, result)
    return list(result.keys())

def __get_parens(number, result):
    if number == 1:
        result["()"] = 0
        return
    __get_parens(number-1, result)
    temp = result.copy()
    for item in temp:
        result["()" + item] = 0
        result["(" + item + ")"] = 0
        result[item + "()"] = 0
        del result[item]

class Test(unittest.TestCase):
    def test_parens_by_moving(self):
        self.assertListEqual(get_parens(1), ['()'])
        self.assertListEqual(get_parens(2), ['()()', '(())'])
        self.assertListEqual(get_parens(3), ['()()()', '(()())', '()(())', '((()))', '(())()'])


if __name__ == "__main__":
    unittest.main()