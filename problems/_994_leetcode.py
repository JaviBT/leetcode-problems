# 994. Rotting Oranges
# https://leetcode.com/problems/rotting-oranges

# Solution by: Javi Barranco

# Problem:
# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

from collections import deque

class Solution:
    def orangesRotting(self, grid: [[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: q.append((i, j))

        cnt = -1
        while q:
            qLen = len(q)
            for _ in range(qLen):
                i, j = q.popleft()

                for i_delta, j_delta in [[1,0], [-1,0], [0,1], [0,-1]]:
                    ni, nj = i + i_delta, j + j_delta
                    if (ni < 0 or nj < 0 or
                        ni >= m or nj >= n or
                        grid[ni][nj] == 2 or grid[ni][nj] == 0): continue
                    grid[ni][nj] = 2
                    q.append((ni, nj))

            cnt += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: return -1

        return cnt if cnt != -1 else 0


class Solution2:
    def orangesRotting(self, grid: [[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()

        freshCnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: q.append((i, j))
                elif grid[i][j] == 1: freshCnt += 1
        if freshCnt == 0: return 0

        cnt = -1
        freshCnt += len(q)
        while q:
            qLen = len(q)
            freshCnt -= qLen 
            for _ in range(qLen):
                i, j = q.popleft()

                for i_delta, j_delta in [[1,0], [-1,0], [0,1], [0,-1]]:
                    ni, nj = i + i_delta, j + j_delta
                    if (ni < 0 or nj < 0 or
                        ni >= m or nj >= n or
                        grid[ni][nj] == 2 or grid[ni][nj] == 0): continue
                    grid[ni][nj] = 2
                    q.append((ni, nj))

            cnt += 1

        return cnt if freshCnt == 0 else -1
    

exercise = Solution()

input = [[2,1,1],[1,1,0],[0,1,1]]

expected_output = 4

output = exercise.orangesRotting(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")