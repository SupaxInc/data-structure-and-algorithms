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

## Preorder

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

## Inorder

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

## Postorder

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

### Level Order

```python
def levelOrderTraversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])  # Initialize queue with root node
    
    while queue:
        level_size = len(queue)  # Number of nodes at the current level
        current_level = []  # List to store nodes of the current level
        
        for _ in range(level_size):
            node = queue.popleft()  # Remove and return the leftmost node
            current_level.append(node.val)  # Add the node's value to the current level list
            
            # Add the node's children to the queue for future processing
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)  # Add the current level list to the result list
    
    return result
```

# Different Facts about the Traversals

## **Preorder Traversal (Node, Left, Right)**

- **First Value**: The first value in a preorder traversal is always the root of the tree.
- **Root-Subtree Relationship**: Preorder traversal provides a straightforward way to understand the root-subtree relationships in the tree. The order reflects how subtrees are encountered relative to each root node.
- **Reconstruction**: Given a preorder traversal along with one of the other traversals (inorder or postorder), it's possible to uniquely reconstruct the binary tree.

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