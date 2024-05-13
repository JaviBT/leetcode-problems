# 1584. Min Cost to Connect All Points
# https://leetcode.com/problems/min-cost-to-connect-all-points

# Solution by: Javi Barranco

# Problem:
# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|,
# where |val| denotes the absolute value of val.
# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

# Example 1:
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20

from typing import List
import heapq

class Solution: # Using Prim's algorithm
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        e =  { tuple(v) : [] for v in points }

        for v1 in e:
            for v2 in points:
                if tuple(v2) != v1:
                    e[v1].append([abs(v1[0] - v2[0]) + abs(v1[1] - v2[1]), tuple(v2)])

        minHeap = [(0, tuple(points[0]))]
        visited = set()
        total = 0

        while len(visited) < len(points):
            dist, p = heapq.heappop(minHeap)
            if p in visited: continue

            visited.add(p)
            total += dist

            for dist, v2 in e[tuple(p)]:
                if v2 not in visited:
                    heapq.heappush(minHeap, (dist, v2))

        return total
    

exercise = Solution()

input = [[0,0],[2,2],[3,10],[5,2],[7,0]]

expected_output = 20

output = exercise.minCostConnectPoints(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")