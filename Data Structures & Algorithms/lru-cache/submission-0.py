class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None 
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        #To save key:address
        self.hashMap = {}
        self.capacity = capacity
        self.left =  Node(0, 0)
        self.right = Node(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, nxt = node.prev , node.nxt 
        prev.nxt = nxt
        nxt.prev = prev 
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right 
        prev.nxt = node
        nxt.prev = node 
        node.nxt = nxt 
        node.prev = prev
        
    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
            self.insert(self.hashMap[key])
            return self.hashMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
        self.hashMap[key] = Node(key, value)
        self.insert(self.hashMap[key])

        if len(self.hashMap) > self.capacity:
            lru = self.left.nxt
            self.remove(lru)
            del self.hashMap[lru.key]