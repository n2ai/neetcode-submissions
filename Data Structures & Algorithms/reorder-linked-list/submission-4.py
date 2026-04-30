# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        def reverse(node):
            prev = None
            cur = node
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        l2_start = slow.next
        mid.next = None 
        
        l1 = head
        l2 = reverse(l2_start)

        while l2:
            tmp1 = l1.next
            tmp2 = l2.next

            l1.next = l2 
            l2.next = tmp1

            l1 = tmp1
            l2 = tmp2

        