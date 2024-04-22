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
  

class Solution2:
    def twoSum(self, numbers: [int], target: int) -> [int]:
        # Constant extra-space means we can't use hashmaps/dictionaries
        l, r = 0, len(n) - 1

        while l != r:
            if numbers[l] + numbers[r] == target: return [l + 1, r + 1]
            elif numbers[l] + numbers[r] < target: l += 1
            elif numbers[l] + numbers[r] > target: r -= 1

        return 
    

exercise = Solution()
input = [2,7,11,15]
expected_output = [1,2]
output = exercise.twoSum(input, 9)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
