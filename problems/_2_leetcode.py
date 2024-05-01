# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Solution by: Javi Barranco

# Problem:
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x = 0):
        self.val = x
        self.next = None

def same(l1, l2):
    while l1 != None and l2 != None:
        if l1.val != l2.val: return False
        l1 = l1.next
        l2 = l2.next
    
    if l1 != None or l2 != None: return False
    
    return True


class Solution:
    def addTwoNumbers(self, l1, l2):
        sol = ListNode(0)
        loop = sol
        carry = 0
        
        while l1 != None or l2 != None or carry != 0:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            loop.next = ListNode(carry%10)
            loop = loop.next
            carry //= 10
            
        return sol.next
    

class Solution2:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        res = ListNode()
        cur = res
        carry = 0
        # Sum until one list runs out
        while l1 and l2:
            cur.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = int((l1.val + l2.val + carry) / 10)
            cur = cur.next
            l1, l2 = l1.next, l2.next

        if l1 != None: rem = l1
        else: rem = l2

        # Continue with the remaining list
        while rem != None:
            cur.next = ListNode((rem.val + carry) % 10)
            carry = int((rem.val + carry) / 10)
            cur = cur.next
            rem = rem.next

        # Add final carry
        if carry == 1: cur.next = ListNode(1)

        return res.next
    

exercise = Solution()

input = ListNode(2)
input.next = ListNode(4)
input.next.next = ListNode(3)

input2 = ListNode(5)
input2.next = ListNode(6)
input2.next.next = ListNode(4)

expected_output = ListNode(7)
expected_output.next = ListNode(0)
expected_output.next.next = ListNode(8)

output = exercise.addTwoNumbers(input, input2)
print(output)
assert same(output, expected_output), "Wrong answer"
print("Accepted")
