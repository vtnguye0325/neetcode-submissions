# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        head = None

        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next

        currPtr = head
        while l1 and l2:
            if l1.val < l2.val :
                currPtr.next = l1
                currPtr = l1
                l1=l1.next
            elif l1.val >= l2.val:
                currPtr.next = l2
                currPtr = l2
                l2 = l2.next
        if l1:
            currPtr.next = l1
        if l2:
            currPtr.next = l2

        return head
