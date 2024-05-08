# 332. Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary

# Solution by: Javi Barranco

# Problem:
# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.
# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

# Example:
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]

from typing import List
from collections import defaultdict

class Solution: # Clean and Optimized DFS
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        itinerary = []

        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            itinerary.append(airport)

        dfs("JFK")

        return itinerary[::-1]
    

class Solution2: # Optimized DFS
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        res = []

        for src, dst in tickets:
            adj[src].append(dst)

        for key in adj:
            adj[key].sort()

        def dfs(adj, result, src):
            if src in adj:
                destinations = adj[src][:]
                while destinations:
                    dest = destinations[0]
                    adj[src].pop(0)
                    dfs(adj, res, dest)
                    destinations = adj[src][:]
            res.append(src)

        dfs(adj, res, "JFK")
        res.reverse()

        if len(res) != len(tickets) + 1:
            return []

        return res


class Solution3: # Brute force DFS that Times Out
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        res = []

        ticket_map = {}
        for dep, arr in tickets:
            if dep not in ticket_map:
                ticket_map[dep] = []
            ticket_map[dep].append(arr)

        def dfs(ap: str, n: int):
            res.append(ap)
            if n == 0 and (ap not in ticket_map or not ticket_map[ap]): 
                return True
            if n == 0 or (n > 0 and (ap not in ticket_map or not ticket_map[ap])): 
                return False

            lexi_order_ap = sorted(ticket_map[ap])
            for destination in lexi_order_ap:
                ticket_map[ap].remove(destination)
                if dfs(destination, n - 1): return True
                ticket_map[ap].append(destination)
                res.pop()

            return False
                
        dfs('JFK', n)
        return res
    

class Solution4: # Cleaner - Brute force DFS that Times Out
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = ['JFK']

        tickets.sort()
        ticket_map = { dep: [] for dep, _ in tickets}
        for dep, arr in tickets:
            ticket_map[dep].append(arr)

        def dfs(ap: str):
            if len(res) == len(tickets) + 1: 
                return True
            if ap not in ticket_map:
                return False

            for i, destination in enumerate(ticket_map[ap].copy()):
                ticket_map[ap].pop(i)
                res.append(destination)
                if dfs(destination): return True
                ticket_map[ap].insert(i, destination)
                res.pop()
            
            return False
                
        dfs('JFK')
        return res
    

exercise = Solution()

input = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"], ["JFK","ATL"], ["ATL","JFK"]]

expected_output = ["JFK","ATL","JFK","MUC","LHR","SFO","SJC"]

output = exercise.findItinerary(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")