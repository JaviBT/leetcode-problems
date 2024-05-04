# 881. Boats to Save People
# https://leetcode.com/problems/boats-to-save-people

# Solution by: Javi Barranco

# Problem:
# The i-th person has weight people[i], and each boat can carry a maximum weight of limit.
# Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.
# Return the minimum number of boats to carry every given person. (It is guaranteed each person can be carried by a boat.)

# Example 1:
# Input: people = [1,2], limit = 3
# Output: 1

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        
        while l <= r:
            if people[l] + people[r] <= limit:
                l, r = l + 1, r - 1
            elif people[l] + people[r] > limit:
                r -= 1
            boats += 1

        return boats
    

exercise = Solution()

input = [[1,2], 3]

expected_output = 1

output = exercise.numRescueBoats(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")