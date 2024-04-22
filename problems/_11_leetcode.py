# 11. Container With Most Water

class Solution:
    def maxArea(self, height: [int]) -> int:

        max_area = 0
        a, b = 0, len(height)-1

        while a != b:
            area = (b - a) * min(height[a], height[b])
            if area > max_area: max_area = area

            if height[a] < height[b]:
                a += 1
            else:
                b -= 1

        return max_area

class Solution2: # Timeout
    def maxArea(self, height: [int]) -> int:

        max_area = 0

        for i in range(len(height)):
            for j in range(i+1,len(height)):
                area = (j - i) * min(height[i], height[j])
                if area > max_area: max_area = area
        
        return max_area
    

class Solution3:
    def maxArea(self, height: [int]) -> int:
        l, r = 0, len(height) - 1

        largest = 0

        while l != r:
            area = min(height[l], height[r]) * (r - l)
            largest = max(largest, area)

            if height[l] > height[r]: r -= 1
            else: l += 1

        return largest
    

exercise = Solution()
input = [1,8,6,2,5,4,8,3,7]
expected_output = 49
output = exercise.maxArea(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
