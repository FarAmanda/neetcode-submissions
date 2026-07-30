# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Understand: Given a list, reverse it so that the last element is first
# First element is last, and so on
# Inputs: A singly-linked linked list
# 
# Recommended time complexity: O(n)
# Recommended space: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        if not head:
            return head

        ptr = head
        while ptr is not None:
            arr.append(ptr.val)
            ptr = ptr.next
    
        arr.reverse()
        print(arr)

        ptr = head
        for i in arr:
            ptr.val = i
            ptr = ptr.next

        return head






