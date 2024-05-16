# 111. Minimun Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Solution by: Javi Barranco

# Problem:
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
    
        if left == 0 or right == 0:
            return 1 + left + right
        else:
            return 1 + min(left, right)
        

exercise = Solution()

input = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

expected_output = 2

output = exercise.minDepth(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")