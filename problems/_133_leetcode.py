# 133. Clone Graph
# https://leetcode.com/problems/clone-graph

# Solution by: Javi Barranco

# Problem:
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __eq__(self, other):
        if not other: return False
        return self.val == other.val and all([n1.val == n2.val for n1, n2 in zip(self.neighbors, other.neighbors)])


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        nodeDic = {}
        visited = set()
        bfsQ = deque()
        bfsQ.append(node)

        while bfsQ:
            curNode = bfsQ.popleft()
            visited.add(curNode.val)
            if curNode.val not in nodeDic:
                nodeDic[curNode.val] = Node(curNode.val)
            
            for neighbor in curNode.neighbors:
                if neighbor.val not in visited: 
                    bfsQ.append(neighbor)
                    visited.add(neighbor.val)
                if neighbor.val not in nodeDic:
                    nodeDic[neighbor.val] = Node(neighbor.val)
                nodeDic[curNode.val].neighbors.append(nodeDic[neighbor.val])

        return nodeDic[node.val]
    

exercise = Solution()

input = Node(1, [Node(2), Node(4)])

expected_output = Node(1, [Node(2), Node(4)])

output = exercise.cloneGraph(input)
print(output)
assert Node.__eq__(output, expected_output), "Wrong answer"
print("Accepted")