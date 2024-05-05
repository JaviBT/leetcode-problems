# 55. Jump Game
# https://leetcode.com/problems/jump-game/

# Solution by: Javi Barranco

# Problem:
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true

from typing import List
from collections import deque

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pointer = len(nums) - 1 # Starts pointing at the back
        jump_needed = 0

        while pointer >= 0:
            available_jump = nums[pointer]
            pointer -= 1
            if available_jump >= jump_needed:
                jump_needed = 1
            elif available_jump < jump_needed:
                jump_needed += 1

        if (jump_needed == 1):
            return True
        else:
            return False
        

class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        q = deque()
        q.append(len(nums) - 1)

        while q:
            curIdx = q.popleft()

            for i, idx in enumerate(nums[curIdx-1::-1]):
                if (i + 1) <= idx:
                    q.append(curIdx - 1 - i)
                    if curIdx - 1 - i == 0: return True

        return False
    

class Solution3:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        
        jump_needed = 0
        p = len(nums) - 1

        while p >= 0:
            if nums[p] >= jump_needed:
                jump_needed = 1
            elif nums[p] < jump_needed:
                jump_needed += 1
            p -= 1

        if jump_needed == 1: return True
        else: return False
        
    
exercise = Solution()
input = [2,3,1,1,4]
expected_output = True
output = exercise.canJump(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
