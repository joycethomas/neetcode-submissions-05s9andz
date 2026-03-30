# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the midpoint
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next #fast doesn't really matter here so it doesn't matter if it's None
        '''print(slow.val)'''

        #reverse second half
        prev, second = None, slow.next
        while second: 
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        '''while prev:
            print(prev.val)
            prev = prev.next'''

        #merge - PREV IS HEAD OF SECOND HALF NOW
        slow.next = None
        curr = head
        while prev:
            temp1, temp2 = curr.next, prev.next
            curr.next = prev
            curr = curr.next #now we at 5
            curr.next = temp1
            curr, prev = temp1, temp2
