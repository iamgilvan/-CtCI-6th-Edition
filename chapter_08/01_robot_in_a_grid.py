import unittest

# Time complexity: O(2^(r+c))
# Space complexity: O(r+c)
def get_path(maze):
    if maze is None or len(maze) == 0:
        return None
    path = []
    if __get_path(maze, len(maze) -1, len(maze[0]) -1, path):
        return path
    return None

def __get_path(maze, row, col, path):
    # if out of bounds or not available, return
    if col < 0 or row < 0 or maze[row][col] == -1:
        return False
    is_at_origin = row == 0 and col == 0

    # if there's a path from the start to here, add my location.
    if is_at_origin or __get_path(maze, row, col - 1, path) or __get_path(maze, row - 1, col, path):
        path.append(((row, col)))
        return True

    return False


class Test(unittest.TestCase):
    def setUp(self):
        self.grid = [[0, -1, 0], [0, 0, 0], [-1, 0, 0]]

    def test_find_path(self):
        self.assertListEqual(get_path(self.grid), [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)])

if __name__ == "__main__":
    unittest.main()