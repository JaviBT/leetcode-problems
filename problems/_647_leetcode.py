# 647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings

# Solution by: Javi Barranco

# Problem:
# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes += 1
                l, r = l - 1, r + 1

            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes += 1
                l, r = l - 1, r + 1

        return palindromes
    

exercise = Solution()

input = "abc"

expected_output = 3

output = exercise.countSubstrings(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")