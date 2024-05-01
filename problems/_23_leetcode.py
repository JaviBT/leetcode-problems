# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

# Solution by: Javi Barranco

# Problem:
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]

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
    def mergeKLists(self, lists: [[ListNode]]) -> [ListNode]:
        if not lists: return None
        
        while len(lists) > 1:
            merged = []

            for i in range(0, len(lists), 2):
                merged.append(self.mergeLists(lists[i], lists[i + 1] if i + 1 < len(lists) else []))

            lists = merged

        return lists[0] if lists[0] else None
    
    def mergeLists(self, l1: [[ListNode]], l2: [[ListNode]]) -> [ListNode]:
        res = ListNode()
        cur = res

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        if l1: cur.next = l1
        else: cur.next = l2
    
        return res.next
    

class Solution2:
    def mergeKLists(self, lists: [[ListNode]]) -> [ListNode]:
        if not lists: return None
    
        res = ListNode()
        cur = res

        while True:
            minNode, index = None, 0
            for i, l in enumerate(lists):
                if l and (minNode == None or minNode.val > l.val):
                    minNode = ListNode(l.val)
                    index = i
            if not lists[index]: return None
            lists[index] = lists[index].next

            cur.next = minNode
            cur = cur.next

            noneFlag = True
            for l in lists:
                if l is not None: 
                    noneFlag = False
                    break
            if noneFlag: break
        
        return res.next
    

exercise = Solution()

input = [[ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]]

expected_output = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))))))

output = exercise.mergeKLists(*input)
print(output)
assert sameLinkedList(output, expected_output), "Wrong answer"
print("Accepted")