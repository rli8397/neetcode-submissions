# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None 
        htrav = head
        trav1 = list1
        trav2 = list2

        while trav1 != None and trav2 != None:
            val = min(trav1.val, trav2.val)
            if trav1.val <= trav2.val:
                trav1 = trav1.next
            else: 
                trav2 = trav2.next

            if head == None:
                head = ListNode(val, None)
                htrav = head 
            else: 
                htrav.next = ListNode(val, None)
                htrav = htrav.next  
        
        while trav1 != None:
            if head == None:
                head = ListNode(trav1.val, None)
                htrav = head 
            else: 
                htrav.next = ListNode(trav1.val, None)
                htrav = htrav.next
            trav1 = trav1.next

        while trav2 != None:
            if head == None:
                head = ListNode(trav2.val, None)
                htrav = head 
            else: 
                htrav.next = ListNode(trav2.val, None)
                htrav = htrav.next 
            trav2 = trav2.next      
        
        return head                  