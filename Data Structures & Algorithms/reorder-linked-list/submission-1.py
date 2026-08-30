# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # finds the midpoint 
        mid = head
        fast = head.next
        while fast != None and fast.next != None:
            fast = fast.next.next
            mid = mid.next

        # reverses second half
        mtrav = mid.next
        reverse = mid.next = None

        while mtrav != None:
            rest = mtrav.next
            mtrav.next = reverse
            reverse = mtrav
            mtrav = rest

        # reorder
        trav = head
        mid = reverse
        while mid != None:
            frest = trav.next
            srest = mid.next
            trav.next = mid
            mid.next = frest
            trav = frest
            mid = srest
