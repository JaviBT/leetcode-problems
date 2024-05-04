# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/

# Solution by: Javi Barranco

# Problem:
# Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Example 1:
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda inter: inter[0])
        
        cnt = 0
        lastEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < lastEnd:
                cnt += 1
                lastEnd = min(lastEnd, end)
            else:
                lastEnd = end
        return cnt
    

exercise = Solution()

input = [[1,2],[2,3],[3,4],[1,3]]

expected_output = 1

output = exercise.eraseOverlapIntervals(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")