# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Solution by: Javi Barranco

# Problem:
# Given a string s, find the length of the longest substring without repeating characters.

# Example:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        output = 0
        current_chars = []

        for r in range(len(s)):
            while s[r] in current_chars:
                current_chars = current_chars[1:]
                l += 1
            current_chars.append(s[r])
            output = max(output, r - l + 1)

        return output
        

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        best_len = 1
        l, r = 0, 0

        while r < len(s) - 1:
            # Move window
            r += 1
            new_char = s[r]
            for i in range(l, r):
                if s[i] == s[r]: 
                    l = i+1
                    break

            best_len = max(best_len, r - l + 1)

        return best_len
    

exercise = Solution()
input = "abcabcbb"
expected_output = 3
output = exercise.lengthOfLongestSubstring(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
