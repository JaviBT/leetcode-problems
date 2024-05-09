# 3075. Maximize Happiness of Selected Children
# https://leetcode.com/problems/maximize-happiness-of-selected-children

# Solution by: Javi Barranco

# Problem:
# You are given an array happiness of length n, and a positive integer k.
# There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.
# In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.
# Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.

# Example:
# Input: happiness = [1,2,3,4,5], k = 3
# Output: 9

from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        res = 0

        for turn in range(k):
            res += max((happiness.pop() - turn), 0)

        return res
    

exercise = Solution()

input = [
    [1, 2, 3, 4, 5],
    3
]

expected_output = 9

output = exercise.maximumHappinessSum(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")

