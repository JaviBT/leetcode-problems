# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/

# Solution by: Javi Barranco

# Problem:
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

# Example:
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: [TreeNode], subRoot: [TreeNode]) -> bool:
        if not root: return False
        return self.sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 

    def sameTree(self, p: [TreeNode], q: [TreeNode]) -> bool:
        if p == None and q == None: return True
        elif p == None or q == None: return False

        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right) and (p.val == q.val)
    

exercise = Solution()

input = [TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5),), TreeNode(4, TreeNode(1), TreeNode(2))]

expected_output = True

output = exercise.isSubtree(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")