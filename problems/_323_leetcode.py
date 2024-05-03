# 323. Number of Connected Components in an Undirected Graph
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph

# Solution by: Javi Barranco

# Problem:
# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
# Return the number of connected components in the graph.

# Example 1:
# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2

from typing import List

class Solution: # Union Find 
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n

        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

        for u, v in edges:
            union(u, v)

        return len(set(find(i) for i in range(n))) # Number of parents
        

class Solution2: # DFS on each node
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count
    

exercise = Solution()

input = [5, [[0,1],[1,2],[3,4]]]

expected_output = 2

output = exercise.countComponents(*input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")