# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if head.next is None:   # ✅ Fix 1
            return 


        def reverseLinkedList(node):
            prev = None
            cur = node
            while cur:
                tmp = cur.next
                cur.next = prev 
                prev = cur
                cur = tmp

            return prev 

        cur = head
        while cur.next:
            cur.next = reverseLinkedList(cur.next)
            cur = cur.next
  