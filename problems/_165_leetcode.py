# 165. Compare Version Numbers
# https://leetcode.com/problems/compare-version-numbers

# Solution by: Javi Barranco

# Problem:
# Given two version numbers, version1 and version2, compare them.
# Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character.
# Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.
# To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 1s are equal, but their revision 2 is 0 and 1 respectively, and 0 < 1.
# Return the following:
# - If version1 < version2, return -1.
# - If version1 > version2, return 1.
# - Otherwise, return 0.

# Example 1:
# Input: version1 = "1.01", version2 = "1.001"
# Output: 0

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        lVersion1 = version1.split('.')
        lVersion2 = version2.split('.')

        for i in range(max(len(lVersion1), len(lVersion2))):
            v1 = int(lVersion1[i]) if i < len(lVersion1) else 0
            v2 = int(lVersion2[i]) if i < len(lVersion2) else 0
            
            if v1 < v2: return -1
            if v1 > v2: return 1

        return 0
    

exercise = Solution()

input = "1.01", "1.001"

expected_output = 0

output = exercise.compareVersion(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")