import unittest

def url_ify_pythonic(sentence: str) -> str:
    return sentence.strip().replace(' ', '%20')

# O (N)
def url_ify_algo(sentence: str) -> str:
    txt = ''

    is_first_char = True
    for char in sentence:
        if char != ' ':
            txt += char
            is_first_char = False
            continue
        if char == ' ' and not txt.endswith('%20') and not is_first_char:
            txt += '%20'

    txt = txt.removesuffix('%20')
    return txt

class Test(unittest.TestCase):
    test_cases = {
        ("much ado about nothing      "): "much%20ado%20about%20nothing",
        ("Mr John Smith       "): "Mr%20John%20Smith"
    }

    testable_functions = [
        url_ify_algo, url_ify_pythonic
    ]

    def test_urlify(self):
        for urlify in self.testable_functions:
            for args, expected in self.test_cases.items():
                actual = urlify(args)
                assert actual == expected, f"Failed {urlify.__name__} for: {[args]}"

if __name__ == "__main__":
    unittest.main()