# 86. Partition List
# https://leetcode.com/problems/partition-list/

# Solution by: Javi Barranco

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: [ListNode], x: int) -> [ListNode]:
        if head == None or head.next == None: return head
        
        numbers = []
        node = head
        while node != None:
            numbers.append(node.val)
            node = node.next

        front = []
        back = []
        for num in numbers:
            if num < x:
                front.append(num)
            else:
                back.append(num)
        numbers = front + back

        output = ListNode(numbers[0], None)
        node = output
        for i in range(1, len(numbers)):
            node.next = ListNode(numbers[i], None)
            node = node.next

        return output
    
    def sameLinkedList(self, head1: [ListNode], head2: [ListNode]) -> bool:
        while head1 != None and head2 != None:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        
        return head1 == None and head2 == None
    

exercise = Solution()
input = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
expected_output = ListNode(1, ListNode(2, ListNode(2, ListNode(4, ListNode(3, ListNode(5))))))
output = exercise.partition(input, 3)
print(output)
assert exercise.sameLinkedList(output, expected_output), "Wrong answer"
print("Accepted")
