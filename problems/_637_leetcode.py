# 637. Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Solution by: Javi Barranco

# Problem:
# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
#
# Example:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: [3, 14.5, 11]
#
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11.
# Hence return [3, 14.5, 11].

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: [TreeNode]) -> [float]:
        
        dic = {}

        def averageOfLevelsRec(root: [TreeNode], dic: {}, level: int):
            if root == None: return

            if level in dic.keys():
                dic[level].append(root.val)
            else:
                dic[level] = [root.val]
            
            averageOfLevelsRec(root.left, dic, level+1)
            averageOfLevelsRec(root.right, dic, level+1)

            return 

        def avg(numbers: [int]):
            sum = 0
            for num in numbers:
                sum += num
            return sum / len(numbers)

        averageOfLevelsRec(root, dic, 0)
        return [avg(numbers) for numbers in list(dic.values())]
        

exercise = Solution()

input = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
expected_output = [3, 14.5, 11]

output = exercise.averageOfLevels(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
