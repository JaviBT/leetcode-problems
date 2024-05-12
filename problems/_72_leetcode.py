# 72. Edit Distance
# https://leetcode.com/problems/edit-distance/

# Solution by: Javi Barranco

# Problem:
# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character

# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

class Solution: # 2D DP solution
    def minDistance(self, word1: str, word2: str) -> int:
        row = [len(word2) - i for i in range(len(word2) + 1)]
        
        for i in range(len(word1)):
            new_row = [0] * (len(word2) + 1)
            new_row[-1] = i + 1
            for j in range(len(word2)):
                if word1[-1-i] == word2[-1-j]:
                    new_row[-2-j] = row[-1-j]
                else:
                    new_row[-2-j] = 1 + min(new_row[-1-j], row[-2-j], row[-1-j])
            row = new_row
        
        return row[0]
    

exercise = Solution()

input = [
    "horse",
    "ros"
]

expected_output = 3

output = exercise.minDistance(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")