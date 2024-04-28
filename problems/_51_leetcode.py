# 51. N-Queens
# https://leetcode.com/problems/n-queens

# Solution by: Javi Barranco

# Problem:
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

class Solution:
    def solveNQueens(self, n: int) -> [[str]]:
        cols = set()
        posDiag = set() # (row + col)
        negDiag = set() # (row - col)

        ret = []
        board = [['.'] * n for _ in range(n)]

        def solveNQueensRec(row):
            if row == n:
                ret.append([''.join(char for char in row) for row in board.copy()])
                return

            for col in range(n):
                if col in cols or row + col in posDiag or row - col in negDiag:
                    continue
                
                board[row][col] = 'Q'
                cols.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)

                solveNQueensRec(row + 1)

                board[row][col] = '.'
                cols.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)

        solveNQueensRec(0)
        return ret
    

exercise = Solution()

input = 4

expected_output = [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

output = exercise.solveNQueens(input)
print(output)
assert len(output) == len(expected_output), "Wrong answer"
for out in output:
    assert out in expected_output, "Wrong answer"
print("Accepted")