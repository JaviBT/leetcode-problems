# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/

# Solution by: Javi Barranco

class Solution:
    def minSubArrayLen(self, target: int, nums: [int]) -> int:
        
        valid = False
        output = len(nums)
        current_sum = 0
        l = 0

        for r in range(len(nums)):
            current_sum += nums[r]
            if current_sum >= target: 
                valid = True
                output = min(output, r - l + 1)
            while current_sum >= target:
                current_sum -= nums[l]
                l += 1
                if current_sum >= target:
                    output = min(output, r - l + 1)

        if valid: return output
        else: return 0


exercise = Solution()
input = [2,3,1,2,4,3]
target = 7
expected_output = 2
output = exercise.minSubArrayLen(target, input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
