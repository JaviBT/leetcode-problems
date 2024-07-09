# 1518. Water Bottles
# https://leetcode.com/problems/water-bottles/

# Solution by: Javi Barranco

# Problem:
# Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.
# The operation of drinking a full water bottle turns it into an empty bottle.
# Return the maximum number of water bottles you can drink.

# Example:
# Input: numBottles = 9, numExchange = 3
# Output: 13

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt, emptyBottles = numBottles, 0

        while (numBottles + emptyBottles) >= numExchange:
            tmp = (numBottles + emptyBottles) // numExchange
            emptyBottles = (numBottles + emptyBottles) % numExchange
            numBottles = tmp
            cnt += numBottles

        return cnt
    

exercise = Solution()

input = 9, 3

expected_output = 13

output = exercise.numWaterBottles(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")