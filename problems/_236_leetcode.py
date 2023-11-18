# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Solution by: Javi Barranco

# Problem:
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants
# (where we allow a node to be a descendant of itself).”

# Example:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def lowestCommonAncestorRec(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
            if root == None: return [None, False]
            
            left, status = lowestCommonAncestorRec(root.left, p, q)
            if status == True:
                return [left, True]
            right, status = lowestCommonAncestorRec(root.right, p, q)
            if status == True:
                return [right, True]

            if (p in [root, left, right]) and (q in [root, left, right]):
                return [root, True]
            elif (p in [root, left, right]):
                return [p, False]
            elif (q in [root, left, right]):
                return [q, False]
            return [None, False]

        node, status = lowestCommonAncestorRec(root, p, q)
        return node
    

exercise = Solution()

input = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
p = input.left
q = input.right
expected_output = 3

output = exercise.lowestCommonAncestor(input, p, q)
print(output)
assert output.val == expected_output, "Wrong answer"
print("Accepted")
