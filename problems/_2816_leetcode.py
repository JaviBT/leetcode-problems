# 2816. Double a Number Represented as Linked List
# https://leetcode.com/problems/double-a-number-represented-as-linked-list

# Solution by: Javi Barranco

# Problem:
# You are given a linked list representing a number. The number is in reverse order, such that the head is the least significant digit and the tail is the most significant digit. You need to double this number and return the new linked list.

# Example:
# Input: head = [1,2,3]
# Output: [2,4,6]

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not other: return False
        return self.val == other.val and self.next == other.next
    
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        digits = []

        cur = head
        while cur != None:
            digits.append(cur.val)
            cur = cur.next

        carry = 0
        for i, num in enumerate(digits[::-1]):
            digits[-1 - i] = (num * 2 + carry) % 10
            if (num * 2) // 10 == 1: carry = 1
            else: carry = 0
        if carry == 1: digits = [1] + digits

        head = ListNode(digits[0])
        cur = head
        for digit in digits[1:]:
            cur.next = ListNode(digit)
            cur = cur.next

        return head
    

class Solution2: # Lazy solution won't work for big numbers
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        digits = []

        cur = head
        while cur != None:
            digits.append(str(cur.val))
            cur = cur.next

        digits = str(int(''.join(digits)) * 2)
        head = ListNode(int(digits[0]))
        cur = head
        for digit in digits[1:]:
            cur.next = ListNode(int(digit))
            cur = cur.next

        return head
    

exercise = Solution()

input = ListNode(1, ListNode(2, ListNode(3)))

expected_output = ListNode(2, ListNode(4, ListNode(6)))

output = exercise.doubleIt(input)
print(output)
assert output == expected_output, "Wrong answer"
print("Accepted")