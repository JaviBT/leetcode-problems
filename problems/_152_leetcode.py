# 152. Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray

# Solution by: Javi Barranco

# Problem:
# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# Example:
# Input: nums = [2,3,-2,4]
# Output: 6

import math

class Solution:
    def maxProduct(self, nums: [int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for num in nums:
            if num == 0: 
                curMin, curMax = 1, 1
                continue

            curMin, curMax = min(num * curMin, num * curMax, num), max(num * curMin, num * curMax, num)
            res = max(res, curMax)

        return res
    

class Solution2: # Time out in LeetCode
    def maxProduct(self, nums: [int]) -> int:
        dp = {}

        def maxProductRec(l: int, r: int) -> int:
            if l > r or l >= len(nums): return -math.inf
            if l == r: return nums[l]
            if (l in dp) and (r in dp[l]): return dp[l][r]

            prod = 1
            for num in nums[l: r+1]:
                prod *= num
            if l not in dp: dp[l] = {}
            if r not in dp: dp[l][r] = prod
            dp[l][r] = max(prod, maxProductRec(l,r-1),  maxProductRec(l+1,r))
            
            return dp[l][r]

        return maxProductRec(0, len(nums))
    

exercise = Solution()

input = [2,3,-2,4]

expected_output = 6

output = exercise.maxProduct(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")