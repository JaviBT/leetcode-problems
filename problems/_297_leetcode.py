# 297. Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Solution by: Javi Barranco

# Problem:
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Example:
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

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


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = collections.deque()
        q.append(root)
        tree = []

        # Level Order Traversal
        while q:
            qLen = len(q)
            for i in range(qLen):
                cur = q.popleft()

                if not cur: tree.append('null')
                else: tree.append(str(cur.val))

                if cur:
                    q.append(cur.left)
                    q.append(cur.right)

        while tree and tree[-1] == 'null': tree.pop()
        ret = ','.join(tree)
        return ret

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        levels = collections.deque(data.split(','))

        val = levels.popleft()
        if val == 'null' or val == '': return None
        else: root = TreeNode(int(val))
        
        prev_level = [root]
        new_level = []
        level = 1
        while levels:
            current_node = 0
            for i in range(0, min(2**level, len(levels)), 2):
                if current_node >= len(prev_level): break

                val = levels.popleft()
                new_node = None if val == 'null' else TreeNode(int(val))
                prev_level[current_node].left = new_node
                if new_node: new_level.append(new_node)

                if not levels: break

                val = levels.popleft()
                new_node = None if val == 'null' else TreeNode(int(val))
                prev_level[current_node].right = new_node
                if new_node: new_level.append(new_node)

                current_node += 1
            prev_level = new_level.copy()
            new_level = []
            level += 1
        
        print(root)
        return root
    

exercise = Codec()

input = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))

expected_output = input

output = exercise.deserialize(exercise.serialize(input))
print(output)
assert sameTree(output, expected_output), "Wrong answer"
print("Accepted")