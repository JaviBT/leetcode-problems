# 286. Walls and Gates
# https://leetcode.com/problems/walls-and-gates

# Solution by: Javi Barranco

# Problem:
# You are given an m x n grid rooms initialized with these three possible values.
# - -1 A wall or an obstacle.
# - 0 A gate.
# - INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# Example 1:
# Input: rooms = [
#   [inf,  -1,  0,  inf],
#   [inf, inf, inf,  -1],
#   [inf,  -1, inf,  -1],
#   [0,  -1, inf, inf]
# ]
# Output: [
#   [3,  -1,  0,  1],
#   [2,  2,  1,  -1],
#   [1,  -1, 2,  -1],
#   [0,  -1, 3,  4]

import math
from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        m, n = len(rooms), len(rooms[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n and rooms[x][y] == math.inf:
                    rooms[x][y] = rooms[i][j] + 1
                    q.append((x, y))
        
        return rooms
    

exercise = Solution()

input = [
    [math.inf,  -1,  0,  math.inf],
    [math.inf, math.inf, math.inf,  -1],
    [math.inf,  -1, math.inf,  -1],
    [0,  -1, math.inf, math.inf]
    ]

expected_output = [
    [3,  -1,  0,  1],
    [2,  2,  1,  -1],
    [1,  -1, 2,  -1],
    [0,  -1, 3,  4]
    ]

output = exercise.wallsAndGates(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")