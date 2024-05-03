# 178. Graph Valid Tree
# https://leetcode.com/problems/graph-valid-tree

# Solution by: Javi Barranco

# Problem:
# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
# Return true if the edges of the given graph make up a valid tree, and false otherwise.

# Example 1:
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
    
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor != parent and not dfs(neighbor, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
    

exercise = Solution()

input = [5, [[0,1],[0,2],[0,3],[1,4]]]

expected_output = True

output = exercise.validTree(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")