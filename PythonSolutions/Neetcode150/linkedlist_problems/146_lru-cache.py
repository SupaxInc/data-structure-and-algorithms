class Node:

    def __init__(self, key=0, val=0, next=None,prev=None):
        self.key, self.val = key, val
        self.next, self.prev = next, prev

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.head = Node() # LRU
        self.tail = Node() # MRU
        self.head.next, self.tail.prev = self.tail, self.head

    # Add a node at the tail (MRU)
    def _add(self, node):
        prev, next = self.tail.prev, self.tail
        node.prev = prev
        prev.next = node
        node.next = next
        next.prev = node
        self.cache[node.key] = node # Map the new node to the node's key

    # Remove an existing node from anywhere in the list
    def _remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        del self.cache[node.key]
    
    # Evict a node from the head (LRU)
    def _evict(self):
        lruNode = self.head.next
        self._remove(lruNode)

    # Get a node then add it as the new MRU
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        # Check if key already exists
        if key in self.cache:
            existingNode = self.cache[key]
            self._remove(existingNode)
            existingNode.val = value # Change the value since value can change for an existing key
            self._add(existingNode) # Add the existing node back so its at MRU
        else:
            if len(self.cache) >= self.cap:
                self._evict()
            newNode = Node(key, value)
            self._add(newNode)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)