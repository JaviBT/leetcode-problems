# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/

# Solution by: Javi Barranco

# Problem:
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)² + (y1 - y2)²).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Example:
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]

import heapq
import math

class Node:
    def __init__(self, point: [int]):
        self.x = point[0]
        self.y = point[1]
        self.d_origin = math.sqrt(self.x**2 + self.y**2)

    def __lt__(self, other):
        return self.d_origin < other.d_origin


class Solution:
    def kClosest(self, points: [[int]], k: int) -> [[int]]:
        nodes = [Node(point) for point in points]
        heapq.heapify(nodes)
        
        ret = []
        for _ in range(k):
            node = heapq.heappop(nodes)
            ret.append([node.x, node.y])

        return ret
    

exercise = Solution()

input = [[1,3],[-2,2]]

expected_output = [[-2,2]]

output = exercise.kClosest(input, 1)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")