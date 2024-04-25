# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/

# Solution by: Javi Barranco

# Problem:
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# Example:
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.levels = {}

    def rightSideView(self, root: [TreeNode]) -> [int]:
        self.levelsRec(root, 0)
        return [level[-1] for level in list(self.levels.values())]
    
    def levelsRec(self, root: [TreeNode], level: int) -> None:
        if not root: return

        if level in self.levels: self.levels[level].append(root.val)
        else: self.levels[level] = [root.val]
        self.levelsRec(root.left, level + 1)
        self.levelsRec(root.right, level + 1)


class Solution2:
    def rightSideView(self, root: [TreeNode]) -> [int]:
        rightView = []

        # Level order traversal and then take the last value of each level.
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level: rightView.append(level[-1])

        return rightView



exercise = Solution()

input = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))

expected_output = [1, 3, 4]

output = exercise.rightSideView(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")