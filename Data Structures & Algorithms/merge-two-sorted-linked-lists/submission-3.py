# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        l1 = list1
        l2 = list2


        if l1 and l2:
            if l1.val < l2.val:
                res = l1
                l1 = l1.next
                res.next = None

            else: 
                res = l2
                l2 = l2.next
                res.next = None
        elif l1:
            return l1
        else:
            return l2

        ptr = res

        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
                ptr = ptr.next
                ptr.next = None

            else: 
                ptr.next = l2
                l2 = l2.next
                ptr = ptr.next
                ptr.next = None
        
        if l1:
            ptr.next = l1
        else:
            ptr.next = l2

        return res