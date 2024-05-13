# 778. Swim in Rising Water
# https://leetcode.com/problems/swim-in-rising-water

# Solution by: Javi Barranco

# Problem:
# On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).
# Now rain starts to fall. At time t, the depth of the water everywhere is t.
# You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t.
# You can swim infinite distance in zero time. Of course, you must stay within your boundaries during your swim.
# You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

# Example 1:
# Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Output: 16

from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        visited = set()
        minHeap = [(grid[0][0], (0,0))] # (height, (x, y))

        t = 0
        while True:
        
            while minHeap[0][0] <= t:
                _, (i, j) = heapq.heappop(minHeap)
                visited.add((i, j))
                if i == j == n - 1: return t
                if i + 1 < n and (i + 1, j) not in visited: heapq.heappush(minHeap, (grid[i + 1][j], (i + 1, j)))
                if i - 1 >= 0 and (i - 1, j) not in visited: heapq.heappush(minHeap, (grid[i - 1][j], (i - 1, j)))
                if j + 1 < n and (i, j + 1) not in visited: heapq.heappush(minHeap, (grid[i][j + 1], (i, j + 1)))
                if j - 1 >= 0 and (i, j - 1) not in visited: heapq.heappush(minHeap, (grid[i][j - 1], (i, j - 1)))

            t += 1


exercise = Solution()

input = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]

expected_output = 16

output = exercise.swimInWater(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")