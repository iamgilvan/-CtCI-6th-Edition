
import unittest

def get_towers_of_hanoi(disks_number, source, destination, buffer):
    if disks_number == 0:
        return

    get_towers_of_hanoi(disks_number - 1, source, buffer, destination)
    disk = source.pop()
    destination.append(disk)
    print("Move disk",disks_number,"from rod",source,"to rod",destination)
    get_towers_of_hanoi(disks_number - 1, buffer, destination, source)

class Test(unittest.TestCase):
    def test_towers_of_hanoi(self):
        tower1 = [4, 3, 2, 1]
        tower2 = []
        tower3 = []
        get_towers_of_hanoi(len(tower1), tower1, tower3, tower2)
        self.assertListEqual(tower1, [])
        self.assertListEqual(tower2, [])
        self.assertListEqual(tower3, [4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()