# 417. Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow

# Solution by: Javi Barranco

# Problem:
# You are given an m x n integer matrix heights representing the height of each unit cell in a continent. The Pacific ocean touches the continent's left and top edges, and the Atlantic ocean touches the continent's right and bottom edges.
# Water can only flow in four directions: up, down, left, and right. Water flows from a cell to an adjacent one with an equal or lower height.
# Return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.

# Example 1:
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

class Solution: # DFS
    def pacificAtlantic(self, heights: [[int]]) -> [[int]]:
        m, n = len(heights), len(heights[0])
        visited = {}

        def dfs(i: int, j: int, ocean: int, height: int):
            if (i < 0 or j < 0 or i >= m or j >= n or heights[i][j] < height or visited.get((i,j), [False, False])[ocean] == True):
                return
            
            h = heights[i][j]
            if (i, j) not in visited: visited[(i, j)] = [False, False]
            visited[(i, j)][ocean] = True
            dfs(i + 1, j, ocean, h)
            dfs(i, j + 1, ocean, h)
            dfs(i - 1, j, ocean, h)
            dfs(i, j - 1, ocean, h)

        for col in range(n): # Top Row (Pacific)
            h = heights[0][col]
            dfs(0, col, 0, h) # 0: Pacific, 1: Atlantic

        for row in range(m): # First Col (Pacific)
            h = heights[row][0]
            dfs(row, 0, 0, h)

        for col in range(n): # Bottom Row (Atlantic)
            h = heights[m-1][col]
            dfs(m-1, col, 1, h)

        for row in range(m): # First Col (Pacific)
            h = heights[row][n-1]
            dfs(row, n-1, 1, h)

        res = []
        for i in range(m):
            for j in range(n):
                if visited.get((i,j), [False, False]) == [True, True]: res.append([i, j])
        return res


class Solution: # Brute force DFS
    def pacificAtlantic(self, heights: [[int]]) -> [[int]]:
        m, n = len(heights), len(heights[0])
        visited = set()
        res = []

        def dfs(i: int, j: int):
            if i < -1 or j < -1 or i >= m+1 or j >= n+1 or (i, j) in visited: return (False, False)
            if i < 0 or j < 0: return (True, False)
            elif i >= m or j >= n: return (False, True)
            
            res = [False, False]
            for i_delta, j_delta in [[1,0], [-1,0], [0,1], [0,-1]]:
                ni, nj = i + i_delta, j + j_delta
                if (ni < 0 or nj < 0 or
                    ni >= m or nj >= n or
                    heights[ni][nj] <= heights[i][j]):
                    visited.add((i, j))
                    res = [a or b for a, b in zip(res, dfs(ni, nj))]
                    visited.remove((i, j))

            return res

        for i in range(m):
            for j in range(n):
                pacific, atlantic = dfs(i, j)
                if pacific and atlantic: res.append([i, j])

        return res
    

exercise = Solution()

input = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

expected_output = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

output = exercise.pacificAtlantic(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")