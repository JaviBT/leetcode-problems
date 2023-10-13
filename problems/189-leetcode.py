# 189. Rotate Array

class Solution:
    def rotate(self, nums: [int], k: int) -> None:
        # Check if k is larger than len(nums) and modify it accordingly
        n = len(nums)
        if (k >= n): k = k % n

        nums[:] = list(nums[-k:] + nums[:-k])


exercise = Solution()
input = [1,2,3,4,5,6,7]
k = 3
expected_output = [5,6,7,1,2,3,4]
exercise.rotate(input, k)
output = input
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
