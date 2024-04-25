# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/

# Solution by: Javi Barranco

# Problem:
# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Input: [1,2,3,4,5]
# Output: 3

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: [TreeNode]) -> int:
        return self.diameterOfBinaryTreeRec(root)[1]

    def diameterOfBinaryTreeRec(self, root: [TreeNode]) -> [int]:
        if root == None: return [0, 0]
        left = self.diameterOfBinaryTreeRec(root.left)
        right = self.diameterOfBinaryTreeRec(root.right)
        depth = max(left[0], right[0]) + 1
        diameter = max(left[1], right[1], left[0] + right[0])
        return [depth, diameter]
    

exercise = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
input = root

expected_output = 3

output = exercise.diameterOfBinaryTree(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")