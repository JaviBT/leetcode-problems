# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas

# Solution by: Javi Barranco

# Problem:
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

# Example:
# Input: piles = [3,6,7,11], h = 8
# Output: 4

import math

class Solution:
    def minEatingSpeed(self, piles: [int], h: int) -> int: # => O(nlog(n))
        l, r = 1, max(piles) # O(n)

        while l <= r: # O(log(n))
            k = int(l + (r - l) / 2)
            hours = self.hours_to_eat(piles, k)
            
            if hours > h: l = k + 1
            elif hours <= h: r = k - 1

        return l

    def hours_to_eat(self, piles, k): # O(n)
        hours = 0

        for pile in piles:
            hours += math.ceil(pile / k)

        return hours 
    

exercise = Solution()

input = [[3,6,7,11], 8]

expected_output = 4

output = exercise.minEatingSpeed(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")