# 112. Path Sum
# https://leetcode.com/problems/path-sum/

# Solution by: Javi Barranco

# Problem:
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path
# equals the given sum.
# Note: A leaf is a node with no children.

# Example:
# Given the below binary tree and sum = 22,
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1

# Return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: [TreeNode], targetSum: int) -> bool:
        if root == None: return False
        if root.left == None and root.right == None:
            if root.val == targetSum: return True
    
        return self.hasPathSumRec(root.left, root.val, targetSum) or self.hasPathSumRec(root.right, root.val, targetSum)

    def hasPathSumRec(self, root: [TreeNode], currentSum: int, targetSum: int):
        if root == None: return False
        
        if root.right == None and root.left == None:
            return (currentSum + root.val) == targetSum
        else:
            return self.hasPathSumRec(root.left, currentSum + root.val, targetSum) or self.hasPathSumRec(root.right, currentSum + root.val, targetSum)


exercise = Solution()

input = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1))))
targetSum = 22
expected_output = True

output = exercise.hasPathSum(input, targetSum)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")
