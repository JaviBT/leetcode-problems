# 108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Solution by: Javi Barranco

# Problem:
# Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __balanced_bst__(self):
        def is_bst(node, left, right):
            if not node:
                return True

            if not left < node.val < right:
                return False

            return is_bst(node.left, left, node.val) and is_bst(node.right, node.val, right)
        
        def height(node):
            if not node:
                return 0

            return 1 + max(height(node.left), height(node.right))
        
        return is_bst(self, float('-inf'), float('inf')) and abs(height(self.left) - height(self.right)) <= 1


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def rec(l: int, r: int):
            if l > r:
                return None
            
            cur = TreeNode(nums[(l + r) // 2])
            cur.left = rec(l, (l + r) // 2 - 1)
            cur.right = rec((l + r) // 2 + 1, r)
            return cur

        l, r = 0, len(nums) - 1
        return rec(l, r)
    

exercise = Solution()

input = [-10,-3,0,5,9]

expected_output = True

output = exercise.sortedArrayToBST(input).__balanced_bst__()
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")