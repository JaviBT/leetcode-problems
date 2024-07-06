# 2058. Find the Minimun and Maximun Number of Nodes Between Critical Points
# https://leetcode.com/problems/find-the-minimun-and-maximun-number-of-nodes-between-critical-points

# Solution by: Javi Barranco

# Problem:
# A critical point in a linked list is defined as either a local maxima or a local minima.
# 
# A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.
# 
# A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.
# 
# Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.
# 
# Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical points. If there are fewer than two critical points, return [-1, -1].

# Example:
# Input: head = [5,3,1,2,5,1,2]
# Output: [1, 3]


from typing import List, Optional
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        def isCritical(prev, cur, nxt):
            if prev == None or nxt == None: return False
            if ((prev.val > cur.val and nxt.val > cur.val) or (prev.val < cur.val and nxt.val < cur.val)): return True
            else: return False

        prev = None
        cur = head
        criticals = []
        idx = 0
        min_d, max_d = math.inf, -math.inf

        while cur != None:
            if isCritical(prev, cur, cur.next): 
                if criticals: 
                    min_d = min(min_d, idx - criticals[-1])
                    max_d = max(max_d, idx - criticals[0])
                criticals.append(idx)

            prev = cur
            cur = cur.next
            idx += 1

        if min_d == math.inf: min_d = -1
        if max_d == -math.inf: max_d = -1
        return [min_d, max_d]


class Solution2:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        def isCritical(prev, cur, nxt):
            if prev == None or nxt == None: return False
            if ((prev.val > cur.val and nxt.val > cur.val) or (prev.val < cur.val and nxt.val < cur.val)): return True
            else: return False

        prev = None
        cur = head
        criticals = []
        idx = 0

        while cur != None:
            if isCritical(prev, cur, cur.next): 
                criticals.append(idx)

            prev = cur
            cur = cur.next
            idx += 1

        if len(criticals) < 2: return [-1, -1]

        max_d = criticals[-1] - criticals[0]
        min_d = math.inf

        for i in range(len(criticals) - 1):
            min_d = min(min_d, criticals[i + 1] - criticals[i])

        return [min_d, max_d]


class Solution3: # Brute force solution
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        def isCritical(prev, cur, nxt):
            if prev == None or nxt == None: return False
            if ((prev.val > cur.val and nxt.val > cur.val) or (prev.val < cur.val and nxt.val < cur.val)): return True
            else: return False

        min_d, max_d = math.inf, -math.inf

        prev_s = None
        s = head

        while s != None:
            if isCritical(prev_s, s, s.next):
                dist = 1
                prev_f = s
                f = s.next
                while f != None:
                    if isCritical(prev_f, f, f.next):
                        min_d = min(dist, min_d)
                        max_d = max(dist, max_d)
                    dist += 1

                    prev_f = f
                    f = f.next

            prev_s = s
            s = s.next

        if min_d == math.inf: min_d = -1
        if max_d == -math.inf: max_d = -1
        return [min_d, max_d]
    

exercise = Solution()

input = ListNode(5, ListNode(3, ListNode(1, ListNode(2, ListNode(5, ListNode(1, ListNode(2)))))))

expected_output = [1, 3]

output = exercise.nodesBetweenCriticalPoints(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")