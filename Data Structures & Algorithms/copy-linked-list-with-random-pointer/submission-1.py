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
        
        realToCopy = {}
        copyToReal = {}
        randomMap = {}
        dummy = Node(0)
        #Copy the node first:
        cur = head
        ptr = dummy
        while cur:
            newNode = Node(cur.val)
            realToCopy[cur] = newNode
            copyToReal[newNode] = cur
            randomMap[cur] = cur.random
            ptr.next = newNode
            cur = cur.next 
            ptr = ptr.next
        
        #Loop through the new list
        cur2 = dummy.next

        print(randomMap)

        while cur2:
            random = randomMap[copyToReal[cur2]]
            cur2.random = realToCopy[random] if random else None
            cur2 = cur2.next
        
        return dummy.next
        

    