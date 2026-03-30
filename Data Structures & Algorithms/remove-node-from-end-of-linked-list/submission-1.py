# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #sliding window
        window = 1
        dummy = ListNode(0, head)
        l = dummy
        r = head.next
        while r:
            if window < n:
                r = r.next
                window += 1
            else:
                l = l.next
                r = r.next
        #print(l.val, r. val)
        l.next = l.next.next
        print(l.val)
        
        return dummy.next