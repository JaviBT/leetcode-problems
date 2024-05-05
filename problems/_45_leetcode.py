# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/

# Solution by: Javi Barranco

# Problem:
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.

# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: 2

from typing import List
import math

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0

        l, r = 0, 0
        jumps = 0

        while r < len(nums) - 1:
            for i, num in enumerate(nums[l: r + 1]):
                if i == 0: tmp = r
                r = max(r, l + i + num)
            l = tmp + 1
            jumps += 1

        return jumps
    

class Solution2:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0

        distList = [math.inf] * (len(nums) - 1)
        p = len(nums) - 2

        while p >= 0:
            if nums[p] >=  len(nums) - 1 - p:
                distList[p] = 1
            else:
                if nums[p] > 0: distList[p] = 1 + (min(distList[p + 1: p + nums[p] + 1]) if distList[p + 1: p + nums[p] + 1] else 0)
            p -= 1
        print(distList)
        return distList[0]
    

class Solution3:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0

        cur_segment = set([0])
        next_segment = set()
        jumps = 0

        while len(nums) - 1 not in next_segment:
            next_segment = set()
            for idx in cur_segment:
                for delta in range(1, nums[idx] + 1):
                    next_segment.add(idx + delta)
            cur_segment = next_segment
            jumps += 1

        return jumps
        

class Solution4:
    def jump(self, nums: List[int]) -> int:
        pointer = len(nums) - 1
        jump_needed = 0
        visited_index = []

        while pointer >= 0:
            available_jump = nums[pointer]

            if available_jump >= jump_needed:
                jump_needed = 1

                for jump in range(available_jump, 0, -1):
                    if (pointer + jump) in visited_index:
                        visited_index = [x for x in visited_index if x >= (pointer + jump)]
                        break

                visited_index.append(pointer)
            elif available_jump < jump_needed:
                jump_needed += 1

            pointer -= 1
        
        return len(visited_index) - 1
    

exercise = Solution()
input = [2,3,1,1,4]
expected_output = 2
output = exercise.jump(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
