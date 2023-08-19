import unittest

# Time Complexity: O(M*N), Space Complex: O(M*N) (max depth of stack)
def paint_fill(screen, x, y, new_color):
    if screen[x][y] == new_color:
        return screen
    __paint_fill(screen, x, y, screen[x][y], new_color)
    return screen

def __paint_fill(screen, x, y, old_color, new_color):
    if x < 0 or y < 0 or x >= len(screen) or y >= len(screen[0]):
        return screen
    if screen[x][y] == old_color:
        screen[x][y] = new_color
        __paint_fill(screen, x - 1, y, old_color, new_color)
        __paint_fill(screen, x + 1, y, old_color, new_color)
        __paint_fill(screen, x , y - 1, old_color, new_color)
        __paint_fill(screen, x , y + 1, old_color, new_color)
    return screen

class Test(unittest.TestCase):
    def setUp(self):
        self.screen = [[1, 1, 1, 1],
                        [1, 0, 0, 1],
                        [2, 2, 0, 0],
                        [2, 2, 0, 0]]

    def test_paint_fill(self):
        self.assertListEqual(paint_fill(self.screen, 2, 2, 3),
                                [[1, 1, 1, 1],
                                [1, 3, 3, 1],
                                [2, 2, 3, 3],
                                [2, 2, 3, 3]])


if __name__ == "__main__":
    unittest.main()