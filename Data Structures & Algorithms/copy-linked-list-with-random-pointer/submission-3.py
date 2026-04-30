"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        realToCopy = {None:None}
        cur = head
        while cur:
            newNode = Node(cur.val)
            realToCopy[cur] = newNode

            cur = cur.next 
        
        cur2 = head
        while cur2:
            copyNode = realToCopy[cur2]
            copyNode.next = realToCopy[cur2.next] if cur2.next else None
            copyNode.random = realToCopy[cur2.random] if cur2.random else None

            cur2 = cur2.next 

        return realToCopy[head] 
        

    