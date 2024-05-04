# 253. Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii

# Solution by: Javi Barranco

# Problem:
# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        res, count = 0, 0
        i, j = 0, 0
        while i < len(start):
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res, count)

        return res
    

exercise = Solution()

input = [[0,30],[5,10],[15,20]]

expected_output = 2

output = exercise.minMeetingRooms(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")