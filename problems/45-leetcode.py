# 45. Jump Game II

class Solution:
    def jump(self, nums: [int]) -> int:
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
