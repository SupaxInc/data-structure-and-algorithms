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
        self.head.next, self.tail.prev = self.tail, self.head # Connect the head and tail

    # Add a node at the tail (MRU)
    def _add(self, node):
        prev, next = self.tail.prev, self.tail # Grab the prev and next nodes for the new node
        node.prev = prev # Connect the new node to the previous node of the tail
        prev.next = node # Connect the previous node of the tail to the new node
        node.next = next # Connect the new node's next pointer to the next node (the tail)
        next.prev = node # Connect the tail to the new node
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
            # If the key does not exist then check for the capacity
            if len(self.cache) >= self.cap:
                self._evict() # Evict the LRU since were at capacity
            newNode = Node(key, value) 
            self._add(newNode) # Add new node if were not at capacity

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)