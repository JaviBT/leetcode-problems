# 79. Word Search
# https://leetcode.com/problems/word-search

# Solution by: Javi Barranco

# Problem:
# Given an m x n board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        m, n = len(board[0]), len(board)
        word = [c for c in word]

        def dfs(x: int, y: int, cur: [str]) -> bool:
            if board[y][x] != cur[0]: return False
            elif board[y][x] == cur[0] and len(cur) == 1: return True

            visited[y][x] = True

            found = False
            for x_delta, y_delta in [[0,1], [1,0], [-1,0], [0,-1]]:
                if (x + x_delta) < 0 or (x + x_delta) >= m or (y + y_delta) < 0 or (y + y_delta) >= n: continue
                if visited[y + y_delta][x + x_delta] == True: continue
                found = found or dfs(x + x_delta, y + y_delta, cur[1:])
                if found: 
                    return True
                else:
                    visited[y + y_delta][x + x_delta] = False

        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == word[0]:
                    visited = [[False for _ in range(m)] for _ in range(n)]
                    found = dfs(x, y, word)
                    if found: 
                        return True
                    

exercise = Solution()

input = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

expected_output = True

output = exercise.exist(input, word)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")