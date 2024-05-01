# 2000. Reverse Prefix of Word
# https://leetcode.com/problems/reverse-prefix-of-word/

# Solution by: Javi Barranco

# Problem:
# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

# Example 1:
# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = 0

        while idx < len(word) and word[idx] != ch:
            idx += 1

        if idx < len(word):
            seg = word[0:idx+1]
            word = seg[::-1] + word[idx+1:]

        return word
    

exercise = Solution()

input = ["abcdefd", "d"]

expected_output = "dcbaefd"

output = exercise.reversePrefix(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")