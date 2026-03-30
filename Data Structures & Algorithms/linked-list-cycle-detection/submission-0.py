# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        thanksola = set()
        while head: 
            if head not in thanksola:
                thanksola.add(head)
                head = head.next 
                continue
            else:
                return True
        
        return False