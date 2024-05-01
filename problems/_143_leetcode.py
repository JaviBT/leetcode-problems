# 143. Reorder List
# https://leetcode.com/problems/reorder-list

# Solution by: Javi Barranco

# Problem:
# You are given the head of a singly linked-list. The list can be represented as:
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

# Example 1:
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]

# Define a singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sameLinkedList(head1: [ListNode], head2: [ListNode]) -> bool:
    while head1 != None and head2 != None:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    
    return head1 == None and head2 == None


class Solution:
    def reorderList(self, head: [ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        nodes = []
        while head != None:
            nodes.append(head)
            head = head.next

        zig = False
        i, j = 1, -1
        head = nodes[0]
        curHead = head
        while i - j < len(nodes) + 1:
            if zig:
                curHead.next = nodes[i]
                i += 1
            else:
                curHead.next = nodes[j]
                j -= 1
            zig = not zig
            curHead = curHead.next
        curHead.next = None


exercise = Solution()

input = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

expected_output = ListNode(1, ListNode(4, ListNode(2, ListNode(3))))

exercise.reorderList(input)

output = input
print(output)
assert sameLinkedList(output, expected_output), "Wrong answer"
print("Accepted")