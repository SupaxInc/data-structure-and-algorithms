from typing import Optional
from __future__ import annotations

class Node:
    def __init__(self, key: int = 0, val: int = 0, nxt: Optional[Node] = None, prv: Optional[Node] = None) -> None:
        self.key, self.val = key, val
        self.nxt, self.prv = nxt, prv

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(), Node()
        self.head.nxt = self.tail
        self.tail.prv = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Getting value means its been used so we need to re-add to head
        existingNode = self.cache[key]
        self._remove(existingNode.key)
        self._add(existingNode)

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                self._evict()

            # Create new node and add to linked list/cache
            newNode = Node(key, value)
            self._add(newNode)
        else:
            # Just update value if key exists
            existingNode = self.cache[key]
            existingNode.val = value

            # It's been used again after updating value so remove then add
            self._remove(existingNode.key)
            self._add(existingNode)
    
    def _add(self, node: Node) -> None:
        # Add new node to beginning of head and connect new node to the next node over
        tempNode = self.head.nxt
        self.head.nxt = node
        node.nxt = tempNode
        node.prv = self.head
        tempNode.prv = node

        # Add to cache
        self.cache[node.key] = node

    def _remove(self, key: int) -> None:
        if key not in self.cache:
            return
        
        # Get existing node and remove it from its index in the linked list
        existingNode = self.cache[key]
        prevNode = existingNode.prv
        nextNode = existingNode.nxt
        prevNode.nxt = nextNode
        nextNode.prv = prevNode

        # Remove from cache
        del self.cache[key]
    
    def _evict(self):
        tailNode = self.tail.prv
        self._remove(tailNode.key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# * LRU Cache where the head is the MRU and the tail is LRU, more intuitive: *
class Node:
    def __init__(self, key = 0, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.cap = capacity
        self.cache = {}

        self.head = Node() # MRU
        self.tail = Node() # LRU
        # Initialize the doubly linked list
        self.head.next, self.tail.prev = self.tail, self.head

    def _add(self, node: Node):
        """Add node to head as the new node becomes MRU"""
        prev, next = self.head, self.head.next

        # Connect new node to the old
        node.prev = prev
        node.next = next

        # Connect old nodes to the new node
        next.prev = node
        prev.next = node
        
        self.cache[node.key] = node
    
    def _remove(self, node: Node) -> None:
        """Remove an existing node from anywhere in the doubly linked list"""
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        
        del self.cache[node.key]

    def _evict(self) -> None:
        """Removes the LRU node"""
        lruNode = self.tail.prev
        self._remove(lruNode)

    def get(self, key: int) -> int:
        """Get the node's value based on key and ensure that it is now the MRU."""
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # Turn the found node into MRU
        self._remove(node)
        self._add(node)

        return node.val
        
    def put(self, key: int, value: int) -> None:
        """
        If key exists: Update the value of the node then make it MRU.
        If key doesn't exist: Place new node in the doubly linked list.
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add(node)
        else:
            # Capacity reached, evict the LRU then add the new node
            if len(self.cache) >= self.cap:
                self._evict()
            
            node = Node(key, value)
            self._add(node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)