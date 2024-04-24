# 424. Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/

# Solution by: Javi Barranco

# Problem:
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best_len = 0
        l, r = 0, 0
        char_count = {}

        while r < len(s):
            char = s[r]
            # Update count dictionary
            char_count[char] = char_count.get(char, 0) + 1
            # Slide window if necessary
            while (r - l + 1) - max(list(char_count.values())) > k:
                char_count[s[l]] -= 1
                l += 1
            # Update best_len
            best_len = max(best_len, r - l + 1)
            # Move window forward
            r += 1

        return best_len
    

class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        best_len = 0
        l, r = 0, 0
        char_count = {}

        for r in range(len(s)):
            char = s[r]
            char_count[char] = char_count.get(char, 0) + 1
            while (r - l + 1) - max(list(char_count.values())) > k:
                char_count[s[l]] -= 1
                l += 1
            best_len = max(best_len, r - l + 1)

        return best_len


exercise = Solution()

input = ["ABAB", 2]

expected_output = 4

output = exercise.characterReplacement(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")