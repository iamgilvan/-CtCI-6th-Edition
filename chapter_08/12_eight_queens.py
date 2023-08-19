import unittest

# Time Complexity: O(N!), Space Complexity: O(result*N^2) ??
def solveNQueens(queensNumbers: int):
    column = set()
    posDiag = set() # (r + c)
    negDiag = set() # (r - c)

    result = []
    board = [["."] * queensNumbers for i in range(queensNumbers)]

    def backtrack(row):
        if row == queensNumbers:
            copy = ["".join(row) for row in board]
            result.append(copy)
            return

        for col in range(queensNumbers):
            if col in column or (row + col) in posDiag or (row - col) in negDiag:
                continue
            column.add(col)
            posDiag.add(row + col)
            negDiag.add(row - col)
            board[row][col] = "Q"

            backtrack(row + 1)

            column.remove(col)
            posDiag.remove(row + col)
            negDiag.remove(row - col)
            board[row][col] = "."
    backtrack(0)
    return result

class Test(unittest.TestCase):
    def test_solveNQueens(self):
        self.assertEqual(len(solveNQueens(8)), 92)
        self.assertEqual(len(solveNQueens(4)), 2)

if __name__ == "__main__":
    unittest.main()