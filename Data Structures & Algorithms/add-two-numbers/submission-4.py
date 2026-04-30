# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carried = 0
        dummy = ListNode(0)
        ptr1 = l1
        ptr2 = l2
        cur = dummy
        while ptr1 or ptr2:
            val1 = ptr1.val if ptr1 else 0
            val2 = ptr2.val if ptr2 else 0

            newVal = val1 + val2 + carried
            remain = newVal % 10
            newNode = ListNode(remain)
            cur.next = newNode
            if newVal > 9:
                carried = 1
            else:
                carried = 0
            
            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None
            cur = cur.next

        if carried == 1:
            cur.next = ListNode(carried)

        return dummy.next
        

            