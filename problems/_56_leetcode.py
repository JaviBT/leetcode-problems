# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/

# Solution by: Javi Barranco

# Problem:
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        output = []
        next_interval = []
        intervals.sort(key=lambda x:x[0])

        for i in range(len(intervals)):
            if not next_interval:
                next_interval = intervals[i]
            elif next_interval[1] >= intervals[i][0]:
                next_interval = [min(next_interval[0], intervals[i][0]), max(next_interval[1], intervals[i][1])]
            else:
                output.append(next_interval)
                next_interval = intervals[i]
        output.append(next_interval)

        return output
    

class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1: return intervals
        intervals.sort(key=lambda inter: inter[0])
        
        res = []
        l, r = 0, 1

        while l <= len(intervals) - 1:
            cur_inter = intervals[l]
            while r <= len(intervals) - 1 and (intervals[r][0] <= cur_inter[0] or intervals[r][0] <= cur_inter[1]):
                cur_inter = [min(cur_inter[0], intervals[r][0]), max(cur_inter[1], intervals[r][1])]
                r += 1
            res.append(cur_inter)
            l = r

        return res
    

class Solution3:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1: return intervals
        intervals.sort(key=lambda inter: inter[0])
        
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = res[-1][1]

            if start <= lastEnd:
                res[-1][1] = max(end, lastEnd)
            else:
                res.append([start, end])

        return res
        

exercise = Solution()
input = [[1,3],[2,6],[8,10],[15,18]]
expected_output = [[1,6],[8,10],[15,18]]
output = exercise.merge(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
