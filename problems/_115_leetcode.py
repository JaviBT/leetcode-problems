# 115. Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences

# Solution by: Javi Barranco

# Problem:
# Given two strings s and t, return the number of distinct subsequences of s which equals t.
# A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).
# It is guaranteed the answer fits on a 32-bit signed integer.

# Example 1:
# Input: s = "rabbbit", t = "rabbit"
# Output: 3

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        
        def rec(i: int, j: int):
            if (i, j) in memo: return memo[(i, j)]
            if j >= len(t): return 1
            if i >= len(s): return 0

            res = 0
            res += rec(i+1, j)
            if s[i] == t[j]:
                res += rec(i+1, j+1)

            memo[(i, j)] = res
            return res

        return rec(0, 0)
    

exercise = Solution()

input = [
    "rabbbit",
    "rabbit"
]

expected_output = 3

output = exercise.numDistinct(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")