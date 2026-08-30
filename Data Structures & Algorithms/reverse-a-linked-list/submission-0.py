# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        traverse = head 
        arr = []
        while traverse != None:
            arr.append(traverse.val)
            traverse = traverse.next

        if len(arr) == 0:
            return None

        newHead = ListNode()
        traverse = newHead
        for i in reversed(range(len(arr))):
            traverse.val = arr[i] 
            if i == 0: 
                traverse.next = None
            else: 
                traverse.next = ListNode()
            traverse = traverse.next
        return newHead
