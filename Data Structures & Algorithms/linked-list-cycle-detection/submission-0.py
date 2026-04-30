# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeMap = {}
        nodeArray = []
        cur = head
        while cur:
            if cur.next in nodeMap:
                nodeMap[cur] = cur.next
                break
            nodeMap[cur] = cur.next
            cur = cur.next
            if cur == None:
                return False
            
        return True
        # for i in nodeMap:
        #     nodeArray.append(i)
        
        # tail = nodeArray[len(nodeArray)-1]
        # print(nodeMap)
        # print(nodeArray)
        # return nodeArray.index(nodeMap[tail])


            