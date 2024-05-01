# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Solution by: Javi Barranco

# Problem:
# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

# Example 1:
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

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
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        head = ListNode()
        resHead = head
        
        while list1 or list2:
            if (list2 is None) or (list1 is not None and list1.val <= list2.val):
                head.next = ListNode(list1.val)
                list1 = list1.next
            else:
                head.next = ListNode(list2.val)
                list2 = list2.next
            head = head.next

        return resHead.next
    

exercise = Solution()

input = [ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))]

expected_output = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))

output = exercise.mergeTwoLists(*input)
print(output)
assert sameLinkedList(output, expected_output), "Wrong answer"
print("Accepted")