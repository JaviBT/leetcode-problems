# 105. Construct Binary Tree from Preorder and Inorder Traversal
# htpps://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Solution by: Javi Barranco

# Problem:
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Example:
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sameTree(t1, t2):
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        if t1.val != t2.val: return False

        return sameTree(t1.left, t2.left) and sameTree(t1.right, t2.right)


class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> [TreeNode]:
        if not preorder or not inorder : return None

        root = TreeNode(preorder[0])

        val_index = inorder.index(preorder[0])
        l_num = len(inorder[:val_index])
        
        root.left = self.buildTree(preorder[1:l_num+1], inorder[:val_index])
        root.right = self.buildTree(preorder[l_num+1:], inorder[val_index+1:])

        return root
    

class Solution2:
    def buildTree(self, preorder: [int], inorder: [int]) -> [TreeNode]:
        q = collections.deque(preorder)
        root_val = q.popleft()
        root_index = inorder.index(root_val)
        return TreeNode(root_val, self.buildTreeRec(q, inorder[:root_index]), self.buildTreeRec(q, inorder[root_index+1:]))

    def buildTreeRec(self, preorder: [int], inorder: [int]) -> [TreeNode]:
        if not inorder: return None

        node_val = preorder.popleft()
        node_index = inorder.index(node_val)
        return TreeNode(node_val, self.buildTreeRec(preorder, inorder[:node_index]), self.buildTreeRec(preorder, inorder[node_index+1:]))


exercise = Solution()

input = [3,9,20,15,7]
input2 = [9,3,15,20,7]

expected_output = TreeNode(3)
expected_output.left = TreeNode(9)
expected_output.right = TreeNode(20)
expected_output.right.left = TreeNode(15)
expected_output.right.right = TreeNode(7)

output = exercise.buildTree(input, input2)
print(output)
assert sameTree(output, expected_output), "Wrong answer"
print("Accepted")
