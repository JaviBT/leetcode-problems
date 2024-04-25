# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/

# Solution by: Javi Barranco

# Problem:
# Given a binary tree, determine if it is a valid binary search tree (BST).
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:
# Input: [2,1,3]
# Output: true

# Example 2:
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: [TreeNode]) -> bool:
        return self.isValidBSTRec(root, [-math.inf, math.inf])

    def isValidBSTRec(self, root: [TreeNode], valid_range: [int]) -> bool:
        if not root: return True

        left_cond = root.left is None or root.left.val < root.val
        right_cond = root.right is None or root.right.val > root.val
        root_cond = root.val > valid_range[0] and root.val < valid_range[1]
        cond = left_cond and right_cond and root_cond

        return cond and self.isValidBSTRec(root.left, [valid_range[0], root.val]) and self.isValidBSTRec(root.right, [root.val, valid_range[1]])
    

exercise = Solution()

input = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))

expected_output = False

output = exercise.isValidBST(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")