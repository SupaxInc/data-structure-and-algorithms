# DFS

## Iteratively

### Preorder

Process the node as soon as it's popped. Then, add its right and left children to the stack (right first to ensure left is processed first).

```python
def preorderTraversal(root):
    if not root:
        return []
    
    stack = [root]
    result = []
    
    while stack:
        current = stack.pop()
        result.append(current.val)
        
        # Push right first so that left is processed first
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
    return result
```

### Inorder

The key idea is to go as left as possible, adding nodes to the stack along the way. When you can't go left anymore, process the node and then move right.

```python
def inorderTraversal(root):
    stack = []
    result = []
    current = root
    
    while current or stack:
        # Reach the leftmost node of the current node
        while current:
            stack.append(current)
            current = current.left
        # Current must be None at this point
        current = stack.pop()
        result.append(current.val)  # Add the node to the result
        # We have visited the node and its left subtree. Now, it's right subtree's turn
        current = current.right
    
    return result
```

### Postorder

The postorder is more complex due to its nature. Using two stacks or a reversed modified preorder traversal helps manage the processing order properly.

**Two Stacks Approach:**

```python
def postorderTraversal(root):
    if not root:
        return []
    
    stack1 = [root]
    stack2 = []
    result = []
    
    while stack1:
        current = stack1.pop()
        stack2.append(current)
        
        if current.left:
            stack1.append(current.left)
        if current.right:
            stack1.append(current.right)
    
    while stack2:
        result.append(stack2.pop().val)
    
    return result
```

**Single Stack**

```python
def postorderTraversal(root):
    if not root:
        return []
    
    stack = [root]
    result = []
    
    while stack:
        current = stack.pop()
        result.append(current.val)
        
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    
    # Reverse the result of the modified preorder traversal
    return result[::-1]
```

## Recursively

### Preorder

Visit → Left → Right

```python
def preorderTraversal(root):
    result = []
    def preorder(node):
        if not node:
            return
        result.append(node.val)   # Visit node
        preorder(node.left)       # Traverse left subtree
        preorder(node.right)      # Traverse right subtree
    preorder(root)
    return result
```

### Inorder

Left → Visit → Right

```python
def inorderTraversal(root):
    result = []
    def inorder(node):
        if not node:
            return
        inorder(node.left)        # Traverse left subtree
        result.append(node.val)   # Visit node
        inorder(node.right)       # Traverse right subtree
    inorder(root)
    return result
```

### Postorder

Left → Right → Visit

```python
def postorderTraversal(root):
    result = []
    def postorder(node):
        if not node:
            return
        postorder(node.left)      # Traverse left subtree
        postorder(node.right)     # Traverse right subtree
        result.append(node.val)   # Visit node
    postorder(root)
    return result
```

# BFS

## Iteratively

### **Standard BFS**

**Use Case**: When you need to process all nodes in level-by-level order, like finding the first occurrence of a value.

```python
def bfs_standard(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return result
```

**Real-world example**: Finding the shortest path to a target node or searching for a specific value in a file system tree.

---

### **Level Order Traversal**

**Use Case**: When you need to process nodes level by level and keep track of which level each node belongs to.

```python
def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        level_size = len(queue)  # Important: Capture size before processing level
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(level)
    
    return result
```

**Real-world example**:

- Visualizing an organizational hierarchy
- Printing a family tree generation by generation
- UI rendering of nested components

---

### **Zigzag Level Order**

**Use Case**: When you need to process levels in alternating directions (left-to-right, then right-to-left).

```python
def zigzag_level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        if not left_to_right:
            level.reverse()
            
        result.append(level)
        left_to_right = not left_to_right
    
    return result
```

**Real-world example**:

- Printing data in a snake-like pattern
- Efficient scanning of 2D structures

---

## **Bottom-Up Level Order**

**Use Case**: When you need to process levels from bottom to top.

```python
def level_order_bottom(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.insert(0, level)  # Key difference: insert at beginning
    
    return result
```

**Real-world example**:

- Displaying hierarchical data from most specific to most general
- Showing file system paths from deepest to root

---

### **Right Side View**

**Use Case**: When you need to see what's visible from the right side of the tree.

```python
def right_side_view(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.popleft()
            
            # Only take rightmost node of each level
            if i == level_size - 1:
                result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    return result
```

**Real-world example**:

- Visualizing profile views of hierarchical structures
- Finding boundary nodes in a network

---

### **Level Average**

**Use Case**: When you need to compute averages at each level.

```python
def level_average(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_sum = 0
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(level_sum / level_size)
    
    return result
```

**Real-world example**:

- Computing average salary per level in an organization
- Finding average response time at each network hop

# Different Facts about the Traversals

## **Preorder Traversal (Node, Left, Right)**

- **First Value**: The first value in a preorder traversal is always the root of the tree.
- **Root-Subtree Relationship**: Preorder traversal provides a straightforward way to understand the root-subtree relationships in the tree. The order reflects how subtrees are encountered relative to each root node.
- **Reconstruction**: Given a preorder traversal along with one of the other traversals (inorder or postorder), it's possible to uniquely reconstruct the binary tree.
- The preorder traversal has a different way of propagating values up.
    - You can see this as an example in Leetcode 1448

## **Inorder Traversal (Left, Node, Right)**

- **Sorted Order for BST**: For a Binary Search Tree (BST), the inorder traversal produces nodes in ascending sorted order. This property is unique to BSTs and is a direct result of their left < node < right structure.
- **Middle Value**: The middle value(s) in an inorder traversal can serve as a root for a balanced binary tree if the traversal is from a BST. However, identifying the exact middle depends on the number of nodes (even or odd).
    - For example [9, **3**, 15, 20, 7]
        - 3 is the root node
        - Left side of the 3 are on the left subtree
        - Right side of the 3 are on the right subtree
            - 20 would be the root node
- **Binary Search Tree (BST) Check**: The inorder traversal can be used to verify whether a binary tree is a BST by checking if the traversal order is strictly increasing.

## **Postorder Traversal (Left, Right, Node)**

- **Last Value**: The last value in a postorder traversal is always the root of the tree. This is because, in postorder traversal, we visit the node after its subtrees.
- **Leaf-Root Path**: Postorder traversal effectively describes a path from leaves up to the root, illustrating how the tree can be "assembled" from bottom to top.
- **Subtree Cleanup**: Postorder traversal is particularly useful for operations where you need to deal with subtrees before dealing with the node itself, such as deallocating or deleting nodes from the tree.