# 239. Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum

# Solution by: Javi Barranco

# Problem:
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        res = []
        q = deque()
        l, r = 0, 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if r >= k - 1:
                res.append(nums[q[0]])
                l += 1
            r += 1

        return res
    

class Solution2: # Brute force solution
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        l, r = 0, k
        res = []

        while r <= len(nums):
            res.append(max(nums[l:r]))
            l += 1
            r += 1

        return res
    

exercise = Solution()

input = [1,3,-1,-3,5,3,6,7]

expected_output = [3,3,5,5,6,7]

output = exercise.maxSlidingWindow(input, 3)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")