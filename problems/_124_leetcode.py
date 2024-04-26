# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Solution by: Javi Barranco

# Problem:
# A path in a binary tree is a sequence of nodes where no node is adjacent to the previous node in the sequence. A path can be a single node. Find the maximum path sum of the binary tree.

# Example:
# Input: root = [1,2,3]
# Output: 6

import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
class Solution:
    def maxPathSum(self, root: [TreeNode]) -> int:
        return self.maxPathSumRec(root)[0]

    def maxPathSumRec(self, root: [TreeNode]) -> [int]:
        if not root: return [-math.inf, -math.inf]

        left_best_overall, left_current = self.maxPathSumRec(root.left)
        right_best_overall, right_current = self.maxPathSumRec(root.right)
        current = max(root.val, root.val + right_current, root.val + left_current)
        current_as_root = root.val
        current_as_root = max(current_as_root, current_as_root + left_current)
        current_as_root = max(current_as_root, current_as_root + right_current)
        best_overall = max(left_best_overall, right_best_overall, current, current_as_root)

        return [best_overall, current]
    

exercise = Solution()

input = TreeNode(1, TreeNode(2), TreeNode(3))

expected_output = 6

output = exercise.maxPathSum(input)
print(output)
assert output == expected_output, "Wrong answer" 
print("Accepted")