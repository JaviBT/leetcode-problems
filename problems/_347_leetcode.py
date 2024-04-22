# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

# Solution by: Javi Barranco

# Problem:
# Given a non-empty array of integers, return the k most frequent elements.

# Example:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        count_dict = {}

        for num in nums:
            if num in count_dict.keys():
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        result = list(count_dict.items())
        result.sort(key = lambda x: x[1], reverse=True)
        
        return [x[0] for x in result[:k]]
    

exercise = Solution()

input = [1,1,1,2,2,3]

expected_output = [1,2]

output = exercise.topKFrequent(input, 2)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")