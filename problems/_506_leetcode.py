# 506. Relative Ranks
# https://leetcode.com/problems/relative-ranks

# Solution by: Javi Barranco

# Problem:
# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.
# The athletes are placed based on their scores, where the 1st athlete has the highest score, the 2nd athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:
# The 1st athlete's rank is "Gold Medal".
# The 2nd athlete's rank is "Silver Medal".
# The 3rd athlete's rank is "Bronze Medal".
# For the 4th to nth athlete, their rank is their placement number (i.e., the xth athlete's rank is "x").
# Return an array answer of size n where answer[i] is the rank of the ith athlete.

# Example:
# Input: score = [10,3,8,9,4]
# Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        scoreMap = {}

        for i, val in enumerate(sorted_score):
            if i + 1 == 1: scoreMap[val] = "Gold Medal"
            elif i +1 == 2: scoreMap[val] = "Silver Medal"
            elif i +1 == 3: scoreMap[val] = "Bronze Medal"
            else: scoreMap[val] = f"{i + 1}"

        return [scoreMap[val] for val in score]
    

exercise = Solution()

input = [10,3,8,9,4]

expected_output = ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

output = exercise.findRelativeRanks(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")