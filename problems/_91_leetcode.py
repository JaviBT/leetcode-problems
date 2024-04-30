# 91. Decode Ways
# https://leetcode.com/problems/decode-ways

# Solution by: Javi Barranco

# Problem:
# A message containing letters from A-Z can be encoded into numbers using the following mapping:
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways).
# You must return the number of ways to decode it.

# For example, "11106" can be mapped into:
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
# Given a string s consisting of digits, return the number of ways to decode it.
# The answer is guaranteed to fit in a 32-bit integer.

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        
        def numDecodingsRec(s) -> None:
            if s == '': return 1
            if s in dp:
                return dp[s]

            left = numDecodingsRec(s[1:]) if s[0] != '0' and (len(s) <= 1 or s[1] != '0') else 0
            right = numDecodingsRec(s[2:]) if s[0] != '0' and len(s) > 1 and s[0:2] <= '26' else 0

            dp[s] = left + right
            return dp[s]

        return numDecodingsRec(s)
    

exercise = Solution()

input = "226"

expected_output = 3

output = exercise.numDecodings(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")