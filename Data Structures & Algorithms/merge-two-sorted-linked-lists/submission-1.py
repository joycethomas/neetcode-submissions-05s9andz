# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #try to solve without recursion
        #look at neetcode solution 
        #look at OLA's lecture
        #try recursion
        '''if list1 == None:
            return list2
        elif list2 == None:
            return list1

        if list1.val <= list2.val:
            temp = list1
            temp.next = self.mergeTwoLists(list1.next, list2)
        else:
            temp = list2
            temp.next = self.mergeTwoLists(list1, list2.next)
        return temp'''

        head = ListNode()
        curr = head

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1 != None:
            curr.next = list1
        if list2 != None:
            curr.next = list2
        return head.next

        '''curr1 = list1
        curr2 = list2
        head = list1
        if list1.val > list2.val:
            head = list2
        temp = head

        while curr1 != None or curr2 != None:
            print(curr1.val)
            print(curr2.val)
            if curr1.val < curr2.val:
                temp.next = curr1
                curr1 = curr1.next
            else:
                temp.next = curr2
                curr2 = curr2.next
            temp = temp.next
        
        if curr1 != None: 
            temp.next = curr1
        elif curr2 != None:
            temp.next = curr2
        
        return head'''


        