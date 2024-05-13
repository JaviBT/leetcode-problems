# 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/

# Solution by: Javi Barranco

# Problem:
# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi at the price price_i.
# You are also given three integers src, dst, and k, return the cheapest price from city src to city dst with at most k stops. If there is no such route, return -1.

# Example 1:
# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200

from typing import List
import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [math.inf] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmpPrices = prices.copy()

            for a1, a2, p in flights:
                if prices[a1] < math.inf:
                    tmpPrices[a2] = min(tmpPrices[a2], prices[a1] + p)
        
            prices = tmpPrices.copy()

        return prices[dst] if prices[dst] < math.inf else -1
    

exercise = Solution()

input = 3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1

expected_output = 200

output = exercise.findCheapestPrice(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")