# 452. Minimun Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

# Solution by: Javi Barranco

class Solution:
    def findMinArrowShots(self, points: [[int]]) -> int:
        
        points.sort(key=lambda x: x[0])

        inter = []

        for interval in points:
            if not inter:
                inter.append(interval)
            elif inter[-1][1] >= interval[0]:
                inter[-1] = [max(inter[-1][0], interval[0]), min(inter[-1][1], interval[1])]
            else:
                inter.append(interval)

        return len(inter)
        

exercise = Solution()
input = [[10,16],[2,8],[1,6],[7,12]]
expected_output = 2
output = exercise.findMinArrowShots(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
