# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Solution by: Javi Barranco

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

        print(current_chars)
        return output
        

exercise = Solution()
input = "abcabcbb"
expected_output = 3
output = exercise.lengthOfLongestSubstring(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
