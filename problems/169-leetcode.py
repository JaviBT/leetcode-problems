# 169. Majority Element

class Solution:
    def majorityElement(self, nums: [int]) -> int:
        n = len(nums)
        check = int(n/2)
        numsDict = {}

        for num in nums:
            if num in numsDict:
                numsDict[num] += 1
            else:
                numsDict[num] = 1
        
        for key in numsDict.keys():
            if numsDict[key] > check:
                return key

        return -1
    
exercise = Solution()
input = [2,2,1,1,1,2,2]
expected_output = 2
output = exercise.majorityElement(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
