# 252. Meeting Rooms
# https://leetcode.com/problems/meeting-rooms

# Solution by: Javi Barranco

# Problem:
# Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false

from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        
        lastEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start < lastEnd:
                return False
            lastEnd = end
            
        return True
    

exercise = Solution()

input = [[0,30],[5,10],[15,20]]

expected_output = False

output = exercise.canAttendMeetings(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")