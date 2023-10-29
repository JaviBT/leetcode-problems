# 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Solution by: Javi Barranco

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: [ListNode]) -> [ListNode]:
        if (head == None): return head

        output = head

        while head.next != None:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next

        return output
    
    def same(self, l1, l2):
        while l1 != None and l2 != None:
            if l1.val != l2.val: return False
            l1 = l1.next
            l2 = l2.next
        
        if l1 != None or l2 != None: return False
        
        return True
    

exercise = Solution()

input = ListNode(1)
input.next = ListNode(1)
input.next.next = ListNode(2)

expected_output = ListNode(1)
expected_output.next = ListNode(2)

output = exercise.deleteDuplicates(input)
print(output)
assert exercise.same(output, expected_output), "Wrong answer"
print("Accepted")
