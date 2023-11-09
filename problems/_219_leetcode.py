# 209. Contains Duplicate II

class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        
        index_dic = {}

        for i in range(len(nums)):
            if nums[i] not in index_dic.keys():
                index_dic[nums[i]] = i
            else:
                if abs(index_dic[nums[i]] - i) <= k:
                    return True
                else:
                    index_dic[nums[i]] = i

        return False
    

exercise = Solution()
input = [1,2,3,1]
k = 3
expected_output = True
output = exercise.containsNearbyDuplicate(input, k)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
