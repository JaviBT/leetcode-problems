# 55. Jump Game

class Solution:
    def canJump(self, nums: [int]) -> bool:
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
        
    
exercise = Solution()
input = [2,3,1,1,4]
expected_output = True
output = exercise.canJump(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
