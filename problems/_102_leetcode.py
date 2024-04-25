# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Solution by: Javi Barranco

# Problem:
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Example:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.levels = {}

    def levelOrder(self, root: [TreeNode]) -> [[int]]:
        self.levelOrderRec(root, 0)
        return list(self.levels.values())

    def levelOrderRec(self, root: [TreeNode], level: int) -> None:
        if not root: return

        if level not in self.levels: self.levels[level] = [root.val]
        else: self.levels[level].append(root.val)

        self.levelOrderRec(root.left, level + 1)
        self.levelOrderRec(root.right, level + 1)


exercise = Solution()

input = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

expected_output = [[3], [9, 20], [15, 7]]

output = exercise.levelOrder(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")