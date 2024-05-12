# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/

# Solution by: Javi Barranco

# Problem:
# Given two strings text1 and text2, return the length of their longest common subsequence.
# A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".

# A common subsequence of two strings is a subsequence that is common to both strings.

# Example 1:
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace".

class Solution: # 2D DP solution
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = [0] * (len(text2) + 1)

        for i in range(len(text1)):
            new_row = [0] * (len(text2) + 1)
            for j in range(len(text2)):
                if text1[-1-i] == text2[-1-j]:
                    new_row[-2-j] = 1 + row[-1-j]
                else:
                    new_row[-2-j] = max(new_row[-1-j], row[-2-j])
            row = new_row

        return row[0]


class Solution2: # Recursive solution with memoization
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def rec(i: int, j: int):
            if (i, j) in memo: return memo[(i, j)]
            if i >= len(text1) or j >= len(text2): return 0
            
            res = 0
            if text1[i] != text2[j]:
                res = max(res, rec(i+1, j), rec(i, j+1))
            else:
                res = 1 + max(res, rec(i+1, j+1))

            memo[(i, j)] = res
            return res

        return rec(0, 0)
    

exercise = Solution()

input = [
    "abcde",
    "ace"
]

expected_output = 3

output = exercise.longestCommonSubsequence(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")