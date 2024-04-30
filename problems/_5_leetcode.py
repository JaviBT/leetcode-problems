# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring

# Solution by: Javi Barranco

# Problem:
# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ret = ''
        retLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l, r = l - 1, r + 1
                else: break
            if (r - 1) - (l + 1) + 1 > retLen: 
                ret, retLen = s[l + 1: r], (r - 1) - (l + 1) + 1

            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l, r = l - 1, r + 1
                else: break
            if (r - 1) - (l + 1) + 1 > retLen: 
                ret, retLen = s[l + 1: r], (r - 1) - (l + 1) + 1

        return ret
    

exercise = Solution()

input = "babad"

expected_output = "bab"

output = exercise.longestPalindrome(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")