# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

# Solution by: Javi Barranco

class Solution:
    def numIslands(self, grid: [[str]]) -> int:

        m = len(grid)
        n = len(grid[0])

        visited_matrix = [[False for j in range(n)] for i in range(m)]
        
        count = 0
        for i in range(m):
            for j in range(n):
                if (grid[i][j] == "1") and (visited_matrix[i][j] == False):
                    self.coverIsland(i, j, grid, visited_matrix)
                    count += 1

        return count

        
    def coverIsland(self, x: int, y: int, grid: [[str]], visited_matrix: [[bool]]):
        if (grid[x][y] == "0"): return

        visited_matrix[x][y] = True

        if x - 1 >= 0 and visited_matrix[x-1][y] == False: self.coverIsland(x-1, y, grid, visited_matrix)
        if x + 1 < len(grid) and visited_matrix[x+1][y] == False: self.coverIsland(x+1, y, grid, visited_matrix)
        if y - 1 >= 0 and visited_matrix[x][y-1] == False: self.coverIsland(x, y-1, grid, visited_matrix)
        if y + 1 < len(grid[0]) and visited_matrix[x][y+1] == False: self.coverIsland(x, y+1, grid, visited_matrix)
        return
    

exercise = Solution()
input = [["1","1","1","1","0"],
         ["1","1","0","1","0"],
         ["1","1","0","0","0"],
         ["0","0","0","0","0"]]
expected_output = 1
output = exercise.numIslands(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
