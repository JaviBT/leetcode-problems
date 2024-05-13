# 10. Regular Expression Matching
# https://leetcode.com/problems/regular-expression-matching/

# Solution by: Javi Barranco

# Problem:
# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Example 1:
# Input: s = "aab", p = "c*a*b"
# Output: true

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def rec(i: int, j: int):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            res = i < len(s) and (p[j] == '.' or s[i] == p[j])
            if j + 1 < len(p) and p[j + 1] == '*':
                memo[(i, j)] = (res and rec(i + 1, j)) or rec(i, j + 2)
                return memo[(i, j)]
            if res:
                memo[(i, j)] = rec(i + 1, j + 1)
                return memo[(i, j)]

            memo[(i, j)] = False
            return memo[(i, j)]
            
        return rec(0, 0)
    

exercise = Solution()

input = ["aab", "c*a*b"]

expected_output = True

output = exercise.isMatch(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")