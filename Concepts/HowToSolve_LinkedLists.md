# **What is a Linked List?**

A linked list is a linear data structure where each element (node) contains a reference (link) to the next node in the sequence. Each node typically has two parts: data and a reference to the next node. There are various types of linked lists, including singly linked lists, doubly linked lists, and circular linked lists.

## Different Types

### **1. Singly Linked List**

This is the simplest type of linked list. Each node contains data and a single link field pointing to the next node in the sequence. This structure allows for efficient sequential access and insertion/deletion from the list. However, it does not support efficient reverse traversal or backward access.

**Properties:**

- Traverse in one direction only, from the head to the end.
- Efficient insertion and deletion at the beginning.

**Use Cases:**

- Suitable for applications with high insertion and deletion frequencies near the beginning of the data structure, such as a stack.
- **Template Code**
    
    ```python
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    
    def insert_at_head(head, value):
        new_node = Node(value)
        new_node.next = head
        return new_node
    
    def traverse(head):
        current = head
        while current:
            print(current.value)
            current = current.next
    ```
    

### **2. Doubly Linked List**

In a doubly linked list, each node has two links: one points to the next node and another points to the previous node. This allows for traversal in both directions.

**Properties:**

- Can be traversed both forwards and backwards.
- Insertion and deletion operations are more versatile, allowing for these operations to be conducted more efficiently at both ends and in the middle of the list.

**Use Cases:**

- Useful for applications requiring bidirectional traversal, such as navigation through a web browser history.
- **Template Code**
    
    ```python
    class DNode:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None
    
    def insert_at_head(head, value):
        new_node = DNode(value)
        if head:
            head.prev = new_node
        new_node.next = head
        return new_node
    
    def traverse_forward(head):
        current = head
        while current:
            print(current.value)
            current = current.next
    
    def traverse_backward(tail):
        current = tail
        while current:
            print(current.value)
            current = current.prev
    ```
    

### **3. Circular Linked List**

A circular linked list can be either singly or doubly linked where the last node points back to the first node, making the list circular.

**Properties:**

- There is no "end" of the list, as the last element links back to the first, facilitating a circular traversal.
- Useful for implementing queues where the last node connects back to the first, allowing the queue to be continuously cycled through.

**Use Cases:**

- Often used for managing the allocation of resources shared by multiple processes in a cyclic manner, like round-robin scheduling.
- **Template Code**
    
    ```python
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
    
    def insert_to_circular(head, value):
        new_node = Node(value)
        if not head:
            new_node.next = new_node
            return new_node
        current = head
        while current.next != head:
            current = current.next
        current.next = new_node
        new_node.next = head
        return head
    
    def traverse_circular(head):
        if not head:
            return
        current = head
        while True:
            print(current.value)
            current = current.next
            if current == head:
                break
    ```
    

### **4. Circular Doubly Linked List**

This is a doubly linked list where the head and tail are also connected to each other. This allows for seamless transitions from the head to the tail and vice versa.

**Properties:**

- Combines the benefits of doubly linked lists and circular linked lists.
- Facilitates an efficient traversal and manipulation of nodes at both ends of the list without needing special cases for handling the ends.

**Use Cases:**

- Ideal for applications that require constant access to both ends of the list, such as certain types of advanced data caches or buffers.
- **Template Code**
    
    ```python
    class DNode:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None
    
    def insert_to_circular_doubly(head, value):
        new_node = DNode(value)
        if not head:
            new_node.next = new_node.prev = new_node
            return new_node
        tail = head.prev
        tail.next = new_node
        new_node.prev = tail
        new_node.next = head
        head.prev = new_node
        return head
    
    def traverse_circular_doubly(head):
        if not head:
            return
        current = head
        start = True
        while start or current != head:
            print(current.value)
            current = current.next
            start = False
    ```
    

### **5. Unrolled Linked List**

An unrolled linked list is a variation of the linked list in which each node contains multiple elements, along with a pointer to the next node. This increases node size but decreases the number of nodes, improving cache performance.

**Properties:**

- Nodes contain an array of data elements, reducing overhead and improving cache performance due to fewer pointers and better locality of reference.
- Typically less space-efficient but offers faster sequential access times.

**Use Cases:**

- Useful in database applications where blocks of data need to be frequently accessed together.
- **Template Code**
    
    ```python
    class UnrolledNode:
        def __init__(self, capacity=4):
            self.elements = []
            self.next = None
    
    def insert_in_unrolled(head, value, capacity=4):
        current = head
        if not current:
            return UnrolledNode(capacity)
        while current.next:
            if len(current.elements) < capacity:
                current.elements.append(value)
                return head
            current = current.next
        if len(current.elements) < capacity:
            current.elements.append(value)
        else:
            new_node = UnrolledNode(capacity)
            new_node.elements.append(value)
            current.next = new_node
        return head
    
    def traverse_unrolled(head):
        current = head
        while current:
            for value in current.elements:
                print(value)
            current = current.next
    ```
    

### **6. Skip List**

A skip list is a probabilistic data structure based on multiple layers of linked lists, where each layer is a subset of the layer below, speeding up the search operations to logarithmic time complexity.

**Properties:**

- Combines elements of linked lists and balanced trees.
- Provides efficient average-case operations similar to balanced tree data structures.

**Use Cases:**

- Suitable for applications that require fast search, insert, and delete operations, such as implementing memcached or certain database indexes.

## **Time Complexity**

1. **Accessing Elements:**
    - **Singly and Doubly Linked Lists:** Accessing elements by index in a linked list is generally *O*(*n*) because you have to traverse the list from the head to get to the desired position.
    - **Circular Linked Lists:** Similar to singly or doubly linked lists, accessing elements is *O*(*n*), though traversal might loop back to the start.
2. **Insertion/Deletion:**
    - **At the Head:** *O*(1) for all types of linked lists, as it involves adjusting only a few pointers.
    - **At the Tail or Middle:** *O*(*n*) because you typically need to traverse the list to find the insertion or deletion point.
    - **Doubly Linked Lists:** May still require *O*(*n*) in the worst case to find the position but allows for quicker removals if the node to be removed is already known since you don’t need to find the previous node.
3. **Search:**
    - All types of linked lists generally require *O*(*n*) time to search for an element since you may need to traverse the entire list to find the element.

## **Space Complexity**

- **Overall Space:** For all types of linked lists, the space complexity is *O*(*n*), where *n* is the number of elements in the list. This space is used to store the nodes themselves, each consisting of the data and the required pointers.

# **Best Ways to Solve Linked List Problems**

- **Understanding the Structure:** Be clear about the type of linked list (singly, doubly, or circular).
- **Two-Pointer Techniques:** Often used for cycle detection, finding the middle of the list, or solving problems related to list reversal.
- **Dummy Nodes:** Useful for dealing with edge cases in operations like insertion and deletion, especially at the head of the list.
- **Recursion:** Effective for problems that involve reversing a linked list or copying a complex list with random pointers.
- **Hashing:** Useful for detecting cycles or copying linked lists with complex structures.

## **Use Cases and Common Problem Types**

- **Cycle Detection:** Problems might state "return the node where the cycle begins" or "detect if the list has a cycle."
- **Reversal:** Look for terms like "reverse the list" or "reverse nodes in k-group."
- **Intersection:** Problems may ask where two linked lists intersect or if they intersect.
- **Merge Operations:** Includes merging two sorted linked lists or sorting a linked list using merge sort.
- **Palindrome:** Checking if the list elements form a palindrome.
- Linked lists are particularly efficient for applications where frequent insertions and deletions occur, as these operations do not require the elements to be contiguous in memory, avoiding the need to shift elements as in contiguous data structures like arrays.
    - However, if frequent access to elements by index is required, arrays or other data structures like balanced trees or hash tables might offer better performance due to their *O*(1) or *O*(log*n*) access times.

## **Properties of Linked Lists**

- **Dynamic Size:** The size of the list can change dynamically, which is advantageous for applications where the number of data elements is not known in advance.
- **Ease of Insertion/Deletion:** Inserting or deleting a node does not require the elements to be contiguous in memory, making these operations potentially more efficient than those in an array.

## Algorithms

### Floyd’s Cycle Algorithm

**Concept:**
The algorithm uses two pointers, commonly called **`slow`** and **`fast`**. Both pointers start at the head of the linked list.

**Operation:**

1. **Move the `slow` pointer:** It advances one node at a time.
2. **Move the `fast` pointer:** It advances two nodes at a time.

**Detection:**

- If there is no cycle, the **`fast`** pointer will reach the end of the list (null).
- If there is a cycle, the **`fast`** pointer will eventually overlap with the **`slow`** pointer somewhere within the cycle. This happens because the **`fast`** pointer moves twice as quickly, and it will catch up to the **`slow`** pointer from behind if the list loops back on itself.
- **Template Code**
    
    ```python
    def detect_cycle(head):
        if not head:
            return None  # No cycle if the list is empty
        
        slow = fast = head  # Both pointers start at the head
        
        while fast and fast.next:
            slow = slow.next         # Slow pointer moves one step
            fast = fast.next.next    # Fast pointer moves two steps
            
            if slow == fast:  # A cycle is detected when slow and fast meet
                return True
        
        return False  # If fast reaches the end, there is no cycl
    ```
    

# **Common Template Codes**

**Template for Traversing a Linked List:**

```python
def traverse(head):
    current = head
    while current:
        print(current.val)
        current = current.next

```

**Template for Reversing a Linked List:**

```python
def reverse(head):
    previous = None
    current = head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous

```

**Template for Detecting a Cycle (Floyd’s Cycle-Finding Algorithm):**

```python
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True  # There is a cycle
    return False  # No cycle

```

**Template for Merging Two Sorted Lists:**

```python
def mergeTwoLists(l1, l2):
    dummy = tail = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next

```