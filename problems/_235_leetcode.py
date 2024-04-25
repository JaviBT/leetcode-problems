# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Solution by: Javi Barranco

# Problem:
# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Example:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.answer = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lowestCommonAncestorRec(root, p, q)
        return self.answer
    
    def lowestCommonAncestorRec(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return [False, False] # [p found, q found]

        left_p, left_q = self.lowestCommonAncestorRec(root.left, p, q)
        right_p, right_q = self.lowestCommonAncestorRec(root.right, p, q)
        root_p, root_q = root is p, root is q

        ret = [left_p or right_p or root_p, left_q or right_q or root_q]
        if ret == [True, True] and [left_p, left_q] != [True, True] and [right_p, right_q] != [True, True]:
            self.answer = root
        return ret
    

exercise = Solution()

input = TreeNode(6, TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))), TreeNode(8, TreeNode(7), TreeNode(9)))
input2 = input.left
input3 = input.right

expected_output = input

output = exercise.lowestCommonAncestor(input, input2, input3)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")            