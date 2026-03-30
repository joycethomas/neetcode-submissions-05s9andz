# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or (len(lists) == 1 and len(lists[0]) == 0):
            return None
        if len(lists) == 1:
            return lists[0]

        start = self.merge(lists[0], lists[1])
        if len(lists) == 2:
            return start
            
        for i in range(2, len(lists)):
            start = self.merge(start, lists[i])

        return start

    def merge(self, l1, l2):
        #base cases
        if not l1 and not l2:
            return None
        elif not l2:
            return l1
        elif not l1:
            return l2
        
        #recursive call
        #CHECK IF THIS IS RIGHT (USE LOGIC/DRAW IT OUT)
        if l1.val <= l2.val:
            result = self.merge(l1.next, l2)
            l1.next = result
            return l1
        else:
            result = self.merge(l1, l2.next)
            l2.next = result
            return l2
        
        
        
        