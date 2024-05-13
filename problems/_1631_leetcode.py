# 1631. Path With Minimum Effort
# https://leetcode.com/problems/path-with-minimum-effort/

# Solution by: Javi Barranco

# Problem:
# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

# Example 1:
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2

from typing import List
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])

        minHeap = [(0, 0, 0)] # Jump, row, col
        visited = set()
        max_jump = 0
        
        while minHeap:
            diff, row, col = heapq.heappop(minHeap)
            if (row, col) in visited: continue
            if (row, col) == (n - 1, m - 1):
                return diff
            visited.add((row, col))

            if row - 1 >= 0: heapq.heappush(minHeap, (max(diff, abs(heights[row][col] - heights[row - 1][col])), row - 1, col))
            if row + 1 < n: heapq.heappush(minHeap, (max(diff, abs(heights[row][col] - heights[row + 1][col])), row + 1, col))
            if col - 1 >= 0: heapq.heappush(minHeap, (max(diff, abs(heights[row][col] - heights[row][col - 1])), row, col - 1))
            if col + 1 < m: heapq.heappush(minHeap, (max(diff, abs(heights[row][col] - heights[row][col + 1])), row, col + 1))


exercise = Solution()

input = [[1,2,2],[3,8,2],[5,3,5]]

expected_output = 2

output = exercise.minimumEffortPath(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")