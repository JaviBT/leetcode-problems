# 15. 3Sum

class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:

        nums.sort()
        triplets = []

        for i in range(len(nums)-2):
            a, b = i+1, len(nums)-1
            while a != b:
                if nums[a] + nums[b] == -nums[i]:
                    triplet = [nums[i], nums[a], nums[b]]
                    if triplet not in triplets: triplets.append(triplet)
                
                if nums[a] + nums[b] < -nums[i]:
                    a += 1
                else:
                    b -= 1

        return triplets

class Solution2: #Timeout
    def threeSum(self, nums: [int]) -> [[int]]:

        triplets = []
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        triplet.sort()
                        if triplet not in triplets: triplets.append(triplet)

        return triplets
    

exercise = Solution()
input = [-1,0,1,2,-1,-4]
expected_output = [[-1,-1,2],[-1,0,1]]
output = exercise.threeSum(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
