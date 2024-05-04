# 1851. Minimun Interval to Include Each Query
# https://leetcode.com/problems/minimum-interval-to-include-each-query

# Solution by: Javi Barranco

# Problem:
# You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.
# You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.
# Return an array containing the answers to the queries.

# Example 1:
# Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
# Output: [3,3,1,4]

from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda inter: inter[0])

        minHeap = []
        res = {}
        idx_inter = 0

        for q in sorted(queries):
            # Add relevant intervals to the min heap
            while idx_inter < len(intervals) and intervals[idx_inter][0] <= q:
                heapq.heappush(minHeap, [intervals[idx_inter][1] - intervals[idx_inter][0] + 1, intervals[idx_inter][1]])
                idx_inter += 1

            # Save the min interval that includes q
            while minHeap and minHeap[0][1] < q: heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]
    

class Solution2:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda inter: inter[0])
        queries = [[query, i] for i, query in enumerate(queries)]
        queries.sort(key=lambda query: query[0])

        minHeap = []
        res = [-1] * len(queries)
        idx_inter = 0

        for q, idx in queries:
            # Add relevant intervals to the min heap
            while idx_inter < len(intervals) and intervals[idx_inter][0] <= q:
                heapq.heappush(minHeap, [intervals[idx_inter][1] - intervals[idx_inter][0] + 1, intervals[idx_inter][1]])
                idx_inter += 1

            # Save the min interval that includes q
            while minHeap and minHeap[0][1] < q: heapq.heappop(minHeap)
            if minHeap: res[idx] = minHeap[0][0]

        return res
    

exercise = Solution()

input = [[1,4],[2,4],[3,6],[4,4]], [2,3,4,5]

expected_output = [3,3,1,4]

output = exercise.minInterval(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")