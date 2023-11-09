# 289. Game of Life
# https://leetcode.com/problems/game-of-life/description/

# Solution by: Javi Barranco

class Solution:
    def gameOfLife(self, board: [[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        This solution does use extra space, an alternative would be to use a more complex encoding to store the new state of the board in the same array. For example, (0-3) instead of (0,1).
        """
        newBoard = [[board[i][j] for j in range(len(board[0]))] for i in range(len(board))]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                print("--->", i,j, board[i][j])
                num_neighbors = 0
                for i_offset in range(-1,2,1):
                    for j_offset in range(-1,2,1):
                        if i + i_offset < 0 or i + i_offset >= len(board) or j + j_offset < 0 or j + j_offset >= len(board[0]) or (i_offset == 0 and j_offset == 0): continue
                        print(i + i_offset, j + j_offset, board[i + i_offset][j + j_offset])
                        num_neighbors += board[i + i_offset][j + j_offset]
                print(num_neighbors)
                if board[i][j] == 1:
                    if num_neighbors < 2 or num_neighbors > 3: newBoard[i][j] = 0
                else:
                    if num_neighbors == 3: newBoard[i][j] = 1

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = newBoard[i][j]
                

exercise = Solution()
input = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
expected_output = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
exercise.gameOfLife(input)
output = input
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
