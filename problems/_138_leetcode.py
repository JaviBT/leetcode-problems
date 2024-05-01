# 138. Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/

# Solution by: Javi Barranco

# Problem:
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node.
# Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state.
# None of the pointers in the new list should point to nodes in the original list.

# Example 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Define a singly-linked list
class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def sameLinkedList(head1: [Node], head2: [Node]) -> bool:
    while head1 != None and head2 != None:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    
    return head1 == None and head2 == None


class Solution:
    def copyRandomList(self, head: [Node]) -> [Node]:
        nodeDict = {None:None}

        cur = head
        while cur:
            nodeDict[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            nodeDict[cur].next = nodeDict[cur.next]
            nodeDict[cur].random = nodeDict[cur.random]
            cur = cur.next
        
        return nodeDict[head]


class Solution2:
    def copyRandomList(self, head: [Node]) -> [Node]:
        if head is None: return None

        curHead = head
        nodes = []
        vals = []
        while curHead != None:
            nodes.append(Node(curHead.val))
            vals.append(curHead.val)
            curHead = curHead.next

        curHead = head
        prevNode = None
        for node in nodes:
            if prevNode is not None: prevNode.next = node

            if curHead.random:
                randomHead = curHead.random
                idx = 0
                while randomHead != None:
                    randomHead = randomHead.next
                    idx += 1
                node.random = nodes[len(nodes) - idx]

            curHead = curHead.next
            prevNode = node

        return nodes[0]
    

exercise = Solution()

input = Node(7, Node(13, Node(11, Node(10, Node(1)))))

expected_output = input
                       
output = exercise.copyRandomList(input)
print(output)
assert sameLinkedList(output, expected_output), "Wrong answer"
print("Accepted")