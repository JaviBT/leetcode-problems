# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/

# Solution by: Javi Barranco

# Problem:
# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),
# where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
# We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

# Example 1:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2

from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        e = { v1: [] for v1 in range(1, n + 1) }

        for v1, v2, w in times:
            e[v1].append((w, v2))

        visited = set()
        minHeap = [(0, k)]

        while len(visited) < n:
            if not minHeap: return -1
            delay, cur = heapq.heappop(minHeap)
            visited.add(cur)

            for w, v2 in e[cur]:
                if v2 not in visited:
                    heapq.heappush(minHeap, (delay + w, v2))

        return delay
    

exercise = Solution()

input = [[2,1,1],[2,3,1],[3,4,1]], 4, 2

expected_output = 2

output = exercise.networkDelayTime(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")