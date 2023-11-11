# 117. Populating Next Right Pointers in Each Node II
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

# Solution by: Javi Barranco

# Problem:
# Given a binary tree
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
#
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.

# Example:
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        self.levels = {}

        def connect_add_levels(root: 'Node', level: int):
            if level in self.levels.keys():
                if root: self.levels[level].append(root)
            else:
                if root: self.levels[level] = [root]

            if root:
                connect_add_levels(root.left, level+1)
                connect_add_levels(root.right, level+1)

            return

        connect_add_levels(root, 0)
        
        for level in list(self.levels.keys()):
            for i in range(len(self.levels[level])):
                if i == len(self.levels[level]) - 1: self.levels[level][i].next = None
                else: self.levels[level][i].next = self.levels[level][i+1]

        return root
        

exercise = Solution()

input = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))
expected_output = Node(1, Node(2, Node(4), Node(5)), Node(3, None, Node(7)))
# Connect the nexts
expected_output.left.next = expected_output.right
expected_output.left.left.next = expected_output.left.right
expected_output.left.right.next = expected_output.right.right

def sameTree(t1, t2):
    if not t1 and not t2: return True
    if not t1 or not t2: return False
    if t1.val != t2.val: return False
    if (t1.next == None or t2.next == None):
        if not (t1.next == None and t2.next == None): return False
    else:
        if t1.next.val != t2.next.val: return False

    return sameTree(t1.left, t2.left) and sameTree(t1.right, t2.right)

output = exercise.connect(input)
print(output)
assert sameTree(output, expected_output), "Wrong answer"
print("Accepted")
