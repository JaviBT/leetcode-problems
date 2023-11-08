# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/

# Solution by: Javi Barranco

# Problem:
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Example:
# Input: [1,2,2,3,4,4,3]
# Output: true

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: [TreeNode]) -> bool:
        return self.isSymmetricVal(root.left, root.right)

    def isSymmetricVal(self, a: [TreeNode], b: [TreeNode]):
        if a != None and b != None:
            if a.val == b.val:
                return self.isSymmetricVal(a.left, b.right) and self.isSymmetricVal(a.right, b.left)
        elif a != None or b != None:
            return False
        else:
            return True
        

exercise = Solution()

input = TreeNode(1)
input.left = TreeNode(2)
input.right = TreeNode(2)
input.left.left = TreeNode(3)
input.left.right = TreeNode(4)
input.right.left = TreeNode(4)
input.right.right = TreeNode(3)

expected_output = True

output = exercise.isSymmetric(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
