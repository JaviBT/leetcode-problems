# 36. Valid Sudoku

class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        
        for row in board:
            current = []
            for num in row:
                if (num != "." and num in current): return False
                current.append(num)

        for i in range(9):
            current = []
            for row in board:
                num = row[i]
                if (num != "." and num in current): return False
                current.append(num)

        for i in range(3):
            for j in range(3):
                current = []
                x = i * 3
                y = j * 3
                for x_delta in range(3):
                    for y_delta in range(3):
                        num = board[x + x_delta][y + y_delta]
                        if (num != "." and num in current): return False
                        current.append(num)

        return True
    

exercise = Solution()
input = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]
expected_output = False
output = exercise.isValidSudoku(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
