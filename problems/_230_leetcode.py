# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Solution by: Javi Barranco

# Problem:
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Example:
# Input: root = [3,1,4,null,2], k = 1
# Output: 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: [TreeNode], k: int) -> int:
        ret = []
        self.preorder(root, ret)
        return ret[k-1]
        
    def preorder(self, root: [TreeNode], ret: [int]) -> int:
        if not root: return
        
        self.preorder(root.left, ret)
        ret.append(root.val)
        self.preorder(root.right, ret)


class Solution2:
    def kthSmallest(self, root: [TreeNode], k: int) -> int:
        ret = []
        self.preorder(root, k, ret)
        return ret[k-1]
        
    def preorder(self, root: [TreeNode], k: int, ret: [int]) -> int:
        if not root or k == len(ret): return
        
        self.preorder(root.left, k, ret)
        ret.append(root.val)
        self.preorder(root.right, k, ret)


class Solution3:
    def kthSmallest(self, root: [TreeNode], k: int) -> int:
        # Iterative Solution
        n = 0
        stack = []
        cur = root

        # Left Root Right (inorder)
        while cur or stack:
            # Move left
            while cur:
                stack.append(cur) # Add to visited stack
                cur = cur.left

            cur = stack.pop() # pop from stack when we find None
            n += 1 # Number of visited/processed nodes
            if n == k: return cur.val # If we reached the k-smallest node

            cur = cur.right # Go right after processing node

    
exercise = Solution()

input = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))

expected_output = 1

output = exercise.kthSmallest(input, 1)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")