# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        head = res
        carry = False

        while l1 or l2:
            if not l1:
                l1 = ListNode(0)
            if not l2:
                l2 = ListNode(0)
            print(l1.val, l2.val, carry)
            total = 0
            if carry: 
                total = 1
            carry = False
            total += l1.val + l2.val
            if total >= 10:
                carry = True
                total -= 10
            res.next = ListNode(total, None)
            res = res.next
            l1 = l1.next
            l2 = l2.next
        
        if carry:
            res.next = ListNode(1)
        '''if l1 and not l2: 
            res.next = l1
        if l2 and not l1:
            res.next = l2'''

        return head.next

        