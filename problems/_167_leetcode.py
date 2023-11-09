# 167. Two Sum II - Input array is sorted

class Solution:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        
        a, b = 0, len(numbers)-1

        while a != b:
            if numbers[a] + numbers[b] == target: return [a+1, b+1]

            if numbers[a] + numbers[b] > target:
                b -= 1
            
            if numbers[a] + numbers[b] < target:
                a += 1

        return None
  

exercise = Solution()
input = [2,7,11,15]
expected_output = [1,2]
output = exercise.twoSum(input, 9)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
