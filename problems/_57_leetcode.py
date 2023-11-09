# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/description/

# Solution by: Javi Barranco

class Solution:
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        
        l = []
        r = []
        join_intervals = [newInterval]

        for interval in intervals:
            if interval[1] < newInterval[0]:
                l.append(interval)
            elif interval[0] > newInterval[1]:
                r.append(interval)
            else:
                join_intervals.append(interval)

        return l + [[min([x[0] for x in join_intervals]), max([y[1] for y in join_intervals])]] + r
        

exercise = Solution()
input = [[1,3],[6,9]]
newInterval = [2,5]
expected_output = [[1,5],[6,9]]
output = exercise.insert(input, newInterval)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
