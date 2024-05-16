# 168. Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title

# Solution by: Javi Barranco

# Problem:
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...

# Example 1:
# Input: columnNumber = 701
# Output: "ZY"

import string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        int_map = { (i + 1) % 26 : char for i, char in enumerate(string.ascii_uppercase) }

        res = ''

        while columnNumber > 0:
            res += int_map[(columnNumber % 26)]
            if columnNumber % 26 != 0:
                columnNumber = columnNumber // 26
            else:
                columnNumber = columnNumber / 26 - 1

        return res[::-1]
    

exercise = Solution()

input = 701

expected_output = "ZY"

output = exercise.convertToTitle(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")