# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # pPtr
        # cPtr
        # nPtr

        # pPtr stays 
        # cPtr and nPtr progress
        # nPtr progresses one more time
        # cPtr.next = pPtr
        # disrupting the link
        # p.ptr = cPtr
        # cPtr = nPtr
        # nPtr = nPtr.next
        # loop continues

        if not head:
            return head
        # Setting up, prevPtr, currPtr, & nextPtr
        pPtr = None
        cPtr = head
        nPtr = head

        while cPtr.next is not None:
            nPtr = nPtr.next
            cPtr.next = pPtr
            pPtr = cPtr
            cPtr = nPtr
        
        cPtr.next = pPtr

        return cPtr
