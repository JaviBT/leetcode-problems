# 80. Remove Duplicates from Sorted Array II

class Solution:
    def removeDuplicates(self, nums: int) -> int:
        if len(nums) <= 2:
            return len(nums)

        currentIndex = 2
        for i in range(2, len(nums)):
            if (nums[i] != nums[currentIndex - 2]):
                nums[currentIndex] = nums[i]
                currentIndex += 1

        return currentIndex
    

exercise = Solution()
input = [0,0,0,1,1,1,1,2,2,2,2,2,2,3,3,3,4,4,4,4,4,5,5,6]
expected_output = 13
output = exercise.removeDuplicates(input)
print(output, input[:output])
assert output == expected_output, "Wrong answer"
print("Accepted")
