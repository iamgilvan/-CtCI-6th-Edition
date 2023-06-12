import unittest

def get_ways_to_make_coins(cent):
    coins = [25, 10, 5, 1]
    return __get_ways_to_make_coins(cent, coins, 0)

def __get_ways_to_make_coins(cent, coins, result):
    if cent == 0:
        return result + 1

    for index, coin in enumerate(coins):
        if cent - coin < 0:
            continue
        else:
            result = __get_ways_to_make_coins(cent-coin, coins[index:], result)
    return result


class Test(unittest.TestCase):
    coins = [25, 10, 5, 1]
    def test_coins(self):
        self.assertEqual(get_ways_to_make_coins(15), 6)
        self.assertEqual(get_ways_to_make_coins(53), 49)


if __name__ == "__main__":
    unittest.main()