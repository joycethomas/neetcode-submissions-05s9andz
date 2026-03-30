# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head.next
        l = 1
        while fast and fast.next:
            fast = fast.next.next
            l += 2
        if fast: 
            l += 1
        
        if l == 1:
            return None
        #print('l', l)

        target = l - n
        if target == 0:
            return head.next
        l = 0
        prev = None
        curr = head
        result = head
        while l < target and curr:
            temp = curr.next
            prev = curr
            curr = temp
            l += 1

        temp = curr.next
        #print("prev", prev.val, "curr", curr.val, "temp", temp.val)
        prev.next = temp
        #prev = prev.next
        #print(prev.val)
        return result

        