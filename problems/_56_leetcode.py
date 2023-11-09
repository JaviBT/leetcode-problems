# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/

# Solution by: Javi Barranco

class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        
        output = []
        next_interval = []
        intervals.sort(key=lambda x:x[0])

        for i in range(len(intervals)):
            if not next_interval:
                next_interval = intervals[i]
            elif next_interval[1] >= intervals[i][0]:
                next_interval = [min(next_interval[0], intervals[i][0]), max(next_interval[1], intervals[i][1])]
            else:
                output.append(next_interval)
                next_interval = intervals[i]
        output.append(next_interval)

        return output
        

exercise = Solution()
input = [[1,3],[2,6],[8,10],[15,18]]
expected_output = [[1,6],[8,10],[15,18]]
output = exercise.merge(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
