# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        prevPtr = None
        currPtr = head

        while currPtr:
            tempPtr = currPtr.next
            currPtr.next = prevPtr
            prevPtr = currPtr
            currPtr = tempPtr
        return prevPtr


        