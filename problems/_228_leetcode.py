# 228. Summary Ranges

class Solution:
    def summaryRanges(self, nums: [int]) -> [str]:
        ranges = []
        ret = []
        current = None
        current_range = []

        for i in range(len(nums)):
            if current == None or nums[i] != current + 1:
                if current_range: 
                    current_range.append(nums[i-1])
                    if current_range[0] != current_range[1]:
                        ranges.append("{}->{}".format(current_range[0], current_range[1]))
                    else:
                        ranges.append("{}".format(current_range[0]))
                current_range = [nums[i]]
                current = nums[i]
            elif nums[i] == current + 1:
                current += 1

        if current_range: 
            current_range.append(nums[-1])
            if current_range[0] != current_range[1]:
                ranges.append("{}->{}".format(current_range[0], current_range[1]))
            else:
                ranges.append("{}".format(current_range[0]))

        return ranges
    

exercise = Solution()
input = [0,1,2,4,5,7]
expected_output = ["0->2","4->5","7"]
output = exercise.summaryRanges(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
