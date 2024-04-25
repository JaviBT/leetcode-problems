# 110. Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/

# Solution by: Javi Barranco

# Problem:
# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Example:
# Input: [3,9,20,null,null,15,7]
# Output: true

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: [TreeNode]) -> bool:
        return self.isBalancedRec(root)[1]

    def isBalancedRec(self, root: [TreeNode]) -> bool:
        if root == None: return [0, True]
        left = self.isBalancedRec(root.left)
        right = self.isBalancedRec(root.right)
        return [max(left[0], right[0]) + 1, abs(left[0] - right[0]) <= 1 and left[1] and right[1]]
    

exercise = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
input = root

expected_output = True

output = exercise.isBalanced(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")