class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        #left = LRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left #BUG HERE, PUT SELF.RIGHT.NEXT INSTEAD OF SELF.NEXT.PREV
        self.cachesize = 0
        
    #remove from the list    
    def remove(self, node):
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before
        
    #insert at the end of the linked list
    def insert(self, node):
        tail = self.right.prev
        self.right.prev = tail.next = node
        node.next = self.right
        node.prev = tail

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    #need to add the location of the node as the val
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].val = value
            return
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        self.cachesize += 1

        if self.cachesize > self.cap:
            self.cache.pop(self.left.next.key)
            self.remove(self.left.next)
            self.cachesize -= 1
        
