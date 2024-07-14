# DFS

## DFS in Grid

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/8b2b0921-d690-4e2e-81a6-2684490c0096/Untitled.png)

1. The cell that we are on (blue cell), is directly connected to four different cells (left, right, up, down) due to the **edges** of the cell.
2. We are able to make four recursive calls that goes up, down, right, or left.
    1. **NOTE:** If the corners are also considered as edges, then we must add more conditions.
3. Each cell is specified with: # of row, # of column

### Traversal

***Keep in mind that x is rows and y is column.***

1. Mark the current cell we are on as visited:  `visited[x][y]` 
    1. Prevents the traversal of already visited nodes
2. Before we traverse we need to check if the direction we are going to is valid.
    1. Check if the cell exists
    2. Check if there is a certain condition why we would not want to go to that cell (its a boundary, value we don’t want to traverse to, etc.)
    3. Check if the cell is already visited

### Template Code

```python
def dfs(grid, x, y):
    # Check boundaries and if the current cell is valid for exploration
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or not isValid(grid, x, y):
        return
    
    # Process the current cell
    # For example, mark it as visited (this might vary depending on the problem)
    markAsVisited(grid, x, y)
    
    # Explore neighboring cells (up, down, left, right)
    # Optionally, include diagonals or other specific movements based on the problem
    dfs(grid, x+1, y)  # Down
    dfs(grid, x-1, y)  # Up
    dfs(grid, x, y+1)  # Right
    dfs(grid, x, y-1)  # Left

def isValid(grid, x, y):
    # Implement the condition to determine if the current cell is valid for exploration
    # Example condition: cell is not visited and is of a specific type (e.g., land)
    return grid[x][y] == 1

def markAsVisited(grid, x, y):
    # Mark the cell as visited to avoid revisiting
    # The mechanism to mark it will depend on the problem's requirements
    grid[x][y] = 0  # Example: mark visited cells by changing their value
```

### Example

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/fa06d68f-3ad5-4dfc-960c-68549fb7099a/Untitled.png)

## DFS in Graphs

- Allows to easily solve puzzles since we can backtrack.
- Great for going as deep as possible in a graph to check if something exists.

### Traversal

1. Visiting a vertex
    1. Can begin at any node
2. Exploration of a vertex
    1. Can only visit one node as deep as possible at a time

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/c3933954-71ec-4496-8852-19ce4fbd6eb5/Untitled.png)

How to use DFS to traverse example above:

1. Begin at node 1
    1. Go to node 2
    2. Explore to node 3, no other adjacent vertices, so go back to node 2
2. Now at node 2, go as deep as possible to non-visited nodes
    1. Go to node 7, no other adjacent vertices, go back to 2.
    2. Go to node 6, no other vertices, now go ALL the way back to node 1.
3. Back at node 1
    1. Go to node 5, no where else to go so back to node 1
    2. Go to node 4, no where else
4. We finished and we traversed from 1 → 2 → 7 → 6 → 5 → 4

### Template Code

**Recursive Implementation**

```python
def dfs(graph, node, visited):
    if node in visited:
	    return
    print(node)  # Process the node
    visited.add(node)  # Mark the node as visited
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()  # Use a set to keep track of visited nodes
dfs(graph, 'A', visited)  # Start DFS from node 'A'
```

**Iterative Implementation**

```python
def dfs_iterative(graph, start_node):
    visited = set()  # Keeps track of visited nodes
    stack = [start_node]  # Stack to manage the nodes to be visited next, starting with the start_node
    
    while stack:
        current_node = stack.pop()  # Take the last node added to the stack
        if current_node not in visited:
            print(current_node)  # Process the current node
            visited.add(current_node)  # Mark the current node as visited
            
            # Add unvisited neighbors to the stack
            # Reverse the order of neighbors to match the order of recursive DFS exploration
            neighbors_to_visit = [neighbor for neighbor in graph[current_node] if neighbor not in visited]
            stack.extend(reversed(neighbors_to_visit))

# Example graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Perform DFS starting from node 'A'
dfs_iterative(graph, 'A')
```

### Template Code - Undirected Graph Traversal

```python
def validTree(self, n: int, edges: List[List[int]]) -> bool:
  if not n:
      return True
  
  visited = set()
  graph = {v: [] for v in range(n)}

  # Create an bi-directional graph (undirected)
  for x, y in edges:
      graph[x].append(y)
      graph[y].append(x) # Connect it bi-directionally since its undirected

  def dfs(source, prev):
      # Check if a cycle is detected
      if source in visited:
          return False
      
      visited.add(source)
      for adj in graph[source]:
          # Don't do a DFS on the neighbor we just traversed from since we have visited it already
              # Prevents detecting a cycle this way!!!!!!!
          if adj == prev:
              continue
          
          # Explore the next neighbors and add the current node we are on as the previous
          if not dfs(adj, source):
              return False
      
      return True
  
  # DFS checks if there is a cycle
  # Length of visited checks if all of the vertices are connected
  return dfs(0, -1) and len(visited) == n
```

# BFS

## BFS in Grid

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/286d2a44-ba94-4774-b597-7f8b68e1f095/Untitled.png)

Similar to DFS, we traverse in multiple different directions. Up, right, left, down or corners as well if its part of the requirements

### Traversal

1. Mark visited nodes (cells)
2. Continuously adds all edges to queue
3. Pops the node and checks if the node is valid to traverse to, else continue

Think of it as a burst traversal compared to DFS that goes as deep as possible

### Template Code Normal Traversal

```python
def bfs(grid, start_row, start_col):
    if not isValid(grid, start_row, start_col):
        return  # Starting point is not valid

    # Directions for moving up, down, left, and right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Optionally, include diagonals: directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    queue = deque([(start_row, start_col)])

    while queue:
        row, col = queue.popleft()
        
        # Process the cell at (row, col)...
        if not isValid(grid, new_row, new_col):
		        continue
		   
        markAsVisited(grid, row, col)
        
        # Explore all possible directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            queue.append((new_row, new_col))

def isValid(grid, row, col):
    # Check if (row, col) is within the grid and is a cell we want to explore
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1

def markAsVisited(grid, row, col):
    # Update the cell to indicate it has been visited
    # This example sets visited cells to 0, adapt as needed based on the problem
    grid[row][col] = 0
```

### Template Code Level Order Traversal

```python
from collections import deque

def bfs(grid, start_row, start_col):
    if not isValid(grid, start_row, start_col):
        return  # Starting point is not valid

    # Directions for moving up, down, left, and right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Optionally, include diagonals: directions += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    queue = deque([(start_row, start_col)]) 
    
    # MAKE SURE TO MARK THE BEGINNING NODE AS VISITED
    markAsVisited(grid, start_row, start_col)  # Mark the start position as visited initially

    while queue:
        level_size = len(queue)  # Get the current level size
        for _ in range(level_size):
            row, col = queue.popleft()
            
            # Process the cell at (row, col)...
            # Perform any required action with the current cell, e.g., check, modify
            
            # Explore all possible directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if isValid(grid, new_row, new_col):
                    markAsVisited(grid, new_row, new_col)  # Mark as visited before enqueueing
                    queue.append((new_row, new_col))

def isValid(grid, row, col):
    # Check if (row, col) is within the grid and is a cell we want to explore
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1

def markAsVisited(grid, row, col):
    # Update the cell to indicate it has been visited
    # This example sets visited cells to 0, adapt as needed based on the problem
    grid[row][col] = 0
```

## BFS in Graphs

- Used to find the shortest path
- Traverses through all adjacent vertices

### Traversal

1. Visiting a vertex
    1. Can begin at any node
2. Exploration of a vertex
    1. Visit all adjacent vertices in any order

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/c3933954-71ec-4496-8852-19ce4fbd6eb5/Untitled.png)

How BFS traversal works based on example above:

1. Starting at node 1
    1. Visit all adjacent vertices: 5, 4, 2. 
    2. We can visit in any order.
2. Visit 1 → 2 → 4 → 5
    1. Begin exploration on 2, 4, 5
3. At node 2
    1. Adjacent vertices at 7, 6, 3.
4. At node 4
    1. No other adjacent vertices to traverse to.
5. At node 5
    1. No other adjacent vertices to traverse to.
6. Visit 7 → 6 → 3
    1. No other nodes to explore.
7. We have in visited all nodes 1 → 2 → 4 → 5 → 7 → 6 → 3

### Template Code

```python
from collections import deque, defaultdict

def bfs_directed(graph, start_node):
    visited = set()  # Set to keep track of visited nodes to prevent revisiting
    queue = deque([start_node])  # Initialize a queue with the start node
    
    visited.add(start_node)  # Mark the start node as visited

    while queue:
        current_node = queue.popleft()  # Dequeue a node from the queue
        print(current_node)  # Process the node as needed

        # Enqueue all unvisited neighbors
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)  # Mark the neighbor as visited
                queue.append(neighbor)  # Enqueue the neighbor

# Example usage
graph_directed = defaultdict(list)
edges_directed = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4)]
for u, v in edges_directed:
    graph_directed[u].append(v)  # Only add the edge in one direction for directed graph

print("BFS (Directed Graph):")
bfs_directed(graph_directed, 0)

```

### Template Code - Undirected Graphs

**Undirected graph traversal is the same as BFS directed graph traversal.**

```python
from collections import deque, defaultdict

def bfs_undirected(graph, start_node):
    visited = set()  # Set to keep track of visited nodes to prevent revisiting
    queue = deque([start_node])  # Initialize a queue with the start node
	  
	  # Visit the start node right away
    visited.add(start_node)  # Mark the start node as visited

    while queue:
        current_node = queue.popleft()  # Dequeue a node from the queue
        print(current_node)  # Process the node as needed

        # Enqueue all unvisited neighbors
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)  # Mark the neighbor as visited
                queue.append(neighbor)  # Enqueue the neighbor

# Example usage
graph_undirected = defaultdict(list)
edges_undirected = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4)]
for u, v in edges_undirected:
    graph_undirected[u].append(v)
    graph_undirected[v].append(u)  # Add both directions for undirected graph

print("BFS (Undirected Graph):")
bfs_undirected(graph_undirected, 0)

```

### Template Code - BFS Level Order Traversal

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)

        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                # word[:i], get everything until the index
                # word[i+1:], get everything after index
                # E.g. *ot, h*t, ho*
                pattern = word[:i] + "*" + word[i+1:]
                graph[pattern].append(word) # Undirected graph
        
        queue = deque([beginWord])
        visit = set([beginWord])
        count = 1 # Begin with 1 since we are visiting beginWord right away
        
        # BFS level order traversal
        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                curr = queue.popleft()

                # When we reach the end word, no need to continue
                if curr == endWord:
                    return count
                
                # Create the patterns for the length of current word
                for i in range(len(curr)):
                    pattern = curr[:i] + "*" + curr[i+1:]
                    for nei in graph[pattern]:
                        # Visit the neighbours of the current word patterns
                        if nei not in visit:
                            visit.add(nei)
                            queue.append(nei)
            count += 1
        
        return 0

```

# Famous Algorithms

## Dijkstra + Bellman-Ford

- Used for **Shortest Path** problems for **weighted graphs.**
    - BFS is great for the shortest path problem but one thing it cant do.
        - It completely disregards weight in an edge.

## Bellman-Ford

- More effective solving a shortest path compared to Dijkstra’s algorithm
    - Because it **can accommodate negative weights.**
- Can take a long time to run in terms of complexity.
- **Not the most efficient algorithm.**
    - Worst case is O(n^2)

## Dijkstra

- Also effective at solving a shortest path but does not accommodate
negative weights.
- However, it is a lot faster than Bellman-Ford algorithm and more
efficient.

# Topological Sorting (Top Sort)

Has a runtime complexity of O(Vertices+Edges) time.

## What is it?

It is an ordering of the nodes in a directed graph where for each directed edge from node A to node B, node A appears before node B.

Used to model real world situations that can be represented as a graph with directed edges that has dependencies

- School class prerequisites, example, you can’t take courses that you don’t have prerequisites for.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/cbb2426a-3ad1-46d2-90e1-5112e3ff31d3/Untitled.png)

- Program dependencies, for example, you want to build program J so you would need H and G then E and F then C, B and D and so on.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/6a38b339-7465-4ce6-bb81-8fc02629fd32/Untitled.png)

- Event scheduling

## Directed Acyclic Graphs (DAG)

- The only type of graph that has a valid topological ordering is a Directed Acyclic Graph.
    - To verify that your graph does not contain a cycle, you can use Tarjan’s strongly connected component algorithm to detect cycles.
- Every tree has a topological ordering since they do not contain any cycles

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/d9b7cafd-a96a-46c1-9b91-01b896a9f39f/Untitled.png)

- To see how topological ordering works for a tree, keep picking off leaf nodes in any order until you reach the root node

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/9dd80c24-e450-4f99-8754-43ba02ef7b82/Untitled.png)

## How does the general algorithm work?

1. Pick an unvisited node
2. With the first node, do a DFS exploring only unvisited nodes
3. On the recursive stack pop of the DFS, add the current node to the topological ordering in reverse order.

## Example Traversal

Step 1) Pick Node H

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/a2bc1f8a-5b81-4335-86d4-5b12ea1fe6bb/Untitled.png)

Step 2) DFS and explore unvisited nodes. H → J → M

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/2545d496-68ce-433a-8b97-609913ac922c/Untitled.png)

Step 3) Pop recursive stack of M and backtrack to J and then explore L. Every time stack recursion pops add to topological ordering.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/5b205de6-f7c9-4932-8032-6aaf97fc431c/Untitled.png)

Step 4) Backtrack from L and then to J then back to H.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/290cd49f-4b78-472a-bbaf-42accbb672a7/Untitled.png)

Step 5) From H, visit I and then backtrack to H

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/65f2d1fc-f5e6-46c5-bc93-4613d7e01fc3/Untitled.png)

# Connected Components

## Directed Graphs

### Strongly Connected Components (SCC)

**Definition:** A subset of vertices in a directed graph where every vertex is reachable from every other vertex within the same subset.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/77b85faf-69a1-4fe7-a37b-14a94943c040/Untitled.png)

### Weakly Connected Components (WCC)

**Definition:** A subset of vertices in a directed graph where every vertex is reachable from every other vertex, if the direction of the edges is ignored. It's as if all edges were undirected.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/48741468-ca74-4f08-9514-802a45b61ecb/Untitled.png)

Sometimes weakly connected just means connected but it becomes **weakly** if the directed graph’s vertices are not reachable in other vertices. E.g. A → C cannot be reached above.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/5cdc9b9e-aa13-40d0-9090-ffba0996e170/Untitled.png)

For a graph to be **connected** the underlying graph of a directed graph has to be connected. So the graph above is called **disconnected** since vertices from A to C cannot reach E to F.

## Undirected Graphs

For an undirected graph, connected components are simply the subsets of vertices where each vertex is reachable from every other vertex within the same subset, without considering any directionality of edges (since the edges are undirected). Each component is, in essence, an isolated "island" of connectivity.

```python
    1---2       3
     \ /       / \
      4       5---6
               \
                7
```

In this graph, there are two connected components:

1. **Component 1:** Consists of vertices **`{1, 2, 4}`**. These vertices are all connected to each other directly or indirectly through undirected paths.
2. **Component 2:** Consists of vertices **`{3, 5, 6, 7}`**. These vertices form another separate group where each vertex is reachable from every other vertex in the same group.

## Union Find

# Possible Interview Questions