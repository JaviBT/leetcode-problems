# 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/

# Solution by: Javi Barranco

# Problem:
# We have a collection of stones, each stone has a positive integer weight.
# Each turn, we choose the two heaviest stones and smash them together. Suppose the stones have weights x and y with x <= y. The result of this smash is:
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left. Return the weight of this stone or 0 if there are no stones left.

# Example 1:
# Input: stones = [2,7,4,1,8,1]
# Output: 1

import heapq

class Solution:
    def lastStoneWeight(self, stones: [int]) -> int:
        heap = [-stone for stone in stones] # Make all values negative and use a MinHeap
        heapq.heapify(heap)

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            new_stone = -abs(x - y)

            if new_stone != 0: heapq.heappush(heap, new_stone)

        return abs(heap[0]) if heap else 0
    

exercise = Solution()

input = [2,7,4,1,8,1]

expected_output = 1

output = exercise.lastStoneWeight(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")