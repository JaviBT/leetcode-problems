# 763. Partition Labels
# https://leetcode.com/problems/partition-labels

# Solution by: Javi Barranco

# Problem:
# A string s of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

# Example:
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation: The partition is "ababcbaca", "defegde", "hijhklij".

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        sMap = {}
        for i, char in enumerate(s):
            if char not in sMap: sMap[char] = [i,i]
            else: sMap[char][1] = i

        intervals = sorted(list(sMap.values()))
        merged_intervals = []

        p = 1
        cur_interval = intervals[0]
        while p < len(intervals):
            if intervals[p][0] <= cur_interval[1]:
                cur_interval = [min(cur_interval[0], intervals[p][0]), max(cur_interval[1], intervals[p][1])]
            else:
                merged_intervals.append(cur_interval)
                cur_interval = intervals[p]
            p += 1
        merged_intervals.append(cur_interval)
        
        return [inter[1] - inter[0] + 1 for inter in merged_intervals]
    

exercise = Solution()

input = "ababcbacadefegdehijhklij"

expected_output = [9,7,8]

output = exercise.partitionLabels(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")