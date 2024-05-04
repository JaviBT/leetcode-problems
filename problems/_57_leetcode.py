# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/description/

# Solution by: Javi Barranco

# Problem:
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        l = []
        r = []
        join_intervals = [newInterval]

        for interval in intervals:
            if interval[1] < newInterval[0]:
                l.append(interval)
            elif interval[0] > newInterval[1]:
                r.append(interval)
            else:
                join_intervals.append(interval)

        return l + [[min([x[0] for x in join_intervals]), max([y[1] for y in join_intervals])]] + r
    

class Solution2:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        involvedIntervals = []
        for i, interval in enumerate(intervals):
            if interval[1] < newInterval[0]: continue

            if ((newInterval[0] >= interval[0] and newInterval[0] <= interval[1]) or 
                newInterval[1] >= interval[0] and newInterval[1] <= interval[1] or
                newInterval[0] <= interval[0] and newInterval[1] >= interval[1]):
                involvedIntervals.append(interval)

        involvedIntervals.append(newInterval)
        newInterval = [min([a for a, b in involvedIntervals]), max([b for a, b in involvedIntervals])]
        involvedIntervals.pop()

        res = []
        for i, interval in enumerate(intervals):
            if interval in involvedIntervals: continue
            if newInterval[0] < interval[0] and newInterval not in res:
                res.append(newInterval)
            res.append(interval)
        if newInterval not in res: res.append(newInterval)

        return res
        

exercise = Solution()
input = [[1,3],[6,9]]
newInterval = [2,5]
expected_output = [[1,5],[6,9]]
output = exercise.insert(input, newInterval)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
