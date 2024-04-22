# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

# Solution by: Javi Barranco

# Problem:
# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:
# Input:  [1,2,3,4]
# Output: [24,12,8,6]

class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        left_mult = [1]
        right_mult = [1]

        for i in range(1, len(nums)):
            left_mult.append(nums[i-1]*left_mult[-1])

        for j in range(len(nums)-2,-1,-1):
            right_mult.insert(0, nums[j+1]*right_mult[0])

        for k in range(len(left_mult)):
            left_mult[k] *= right_mult[k]
        
        return left_mult
    

class Solution2:
    def productExceptSelf(self, nums: [int]) -> [int]:
        r_mul = [1]
        l_mul = [1]
        n = len(nums)

        for i in range(n - 1):
            l_pointer = i
            r_pointer = n - i - 1

            l_mul.append(l_mul[-1] * nums[l_pointer])
            r_mul.append(r_mul[-1] * nums[r_pointer])
        
        r_mul.reverse()

        return [r_mul[i] * l_mul[i] for i in range(n)]


class Solution3:
    def productExceptSelf(self, nums: [int]) -> [int]:
        ret = [1]

        # Prefix (Left Multiplication)
        for i in range(1, len(nums)):
            ret.append(ret[-1]*nums[i-1])

        # Postfix (Right Multiplication)
        postfix = 1
        for i in range(0, len(nums)):
            ret[-1-i] *= postfix
            postfix *= nums[-1-i]

        return ret


exercise = Solution()

input = [1,2,3,4]

expected_output = [24,12,8,6]

output = exercise.productExceptSelf(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")