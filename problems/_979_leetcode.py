# 979. Distribute Coins in Binary Tree
# https://leetcode.com/problems/distribute-coins-in-binary-tree

# Solution by: Javi Barranco

# Problem:
# You are given the root of a binary tree with n nodes where each node in the tree has node.val coins.
# There are n coins in total throughout the whole tree.
# In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.
# Return the number of moves required to make every node have exactly one coin.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0
        
        def rec(root: Optional[TreeNode]) -> int:
            nonlocal moves
            if root == None: return [0, 0]
            
            l_coins, l_n = rec(root.left)
            r_coins, r_n = rec(root.right)
            coins = root.val + l_coins + r_coins
            moves += abs(coins - (1 + l_n + r_n))
           
            return [coins, 1 + l_n + r_n]

        rec(root)
        return moves
    

exercise = Solution()

input = TreeNode(3, TreeNode(0, None, None), TreeNode(0, None, None))

expected_output = 2

output = exercise.distributeCoins(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")