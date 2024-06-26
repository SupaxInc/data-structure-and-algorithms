# In-depth Video

Watch Youtube video: https://www.youtube.com/watch?v=wU6udHRIkcc

Disjoint sets and operations

1. Detecting a cycle
2. Graphical Representation
3. Array Representation
4. Weighted Union and Collapsing Find
    1. Helps find root of a tree graph using an array
    2. Direct linking of a node to the direct parent of a set is a collapsing find (e.g, 1 is parent node and it connects 1 → 7 → 8, we can collapse it so that it is 1 → 8 and 1 → 7)

# Union Find

## Complexities

Time Complexity: O(log n)

Best Case Time Complexity with Path Compression and Rank: *O*(*α*(*n*))

Space Complexity: O(n)

- Without optimizations, Union Find **`find`** operations could be *O*(log*n*) in the worst case.
- With path compression and union by rank (or size), the time complexity is improved to *O*(*α*(*n*)), which is nearly constant and much better than *O*(log*n*) for all practical numbers of elements *n*.

## How it Works

From: https://www.youtube.com/watch?v=ayW5B2W9hfo

**Function 1)** `find(x)` Find the group x belongs to

**Function 2)** `union(x, y)` Unions the groups containing x and y

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/68ac88da-2a2d-475d-ac81-695907b7a560/Untitled.png)

**Example)** We can `find(2)` = 0 and `find(3)` = 1, then we can `union(0, 1)` to combine the two groups.

## How to Implement for Graphs

**First Function `find()`**

**Step 1)** Create edges for a vertices and connect them in different groups.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/283334e5-5372-4de7-a6f5-b6388d7d67e6/Untitled.png)

**Step 2)** Designate a representative vertex for the different groups. Representatives finds out if two different vertices belong to the same group.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/a000e0de-9482-41cd-ad24-45bba40b14c9/Untitled.png)

Example: `find(4)` = 0 and `find(2)` = 5

**Second Function `union()`**

**Step 3)** Rearrange the graph so that the groups are now trees.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/04571b3f-2090-43ce-8906-d5206833ae00/Untitled.png)

The root nodes will be the designed representatives. We now have a parent and child representation.

**Step 4)** To find the representative node, we need to traverse up the tree.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/5d8a3055-9935-4499-a112-1f035ee9e26b/Untitled.png)

**Step 5)** To union two trees, we can just set the root of one tree as a child of the other tree.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/21ee997b-5e12-42da-992e-6255a4372063/Untitled.png)

## Code Template

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/e06c837a-8c8c-4049-8a15-22b40037e3a1/Untitled.png)

1. Create the find function, finds the root of the tree.
    1. If the parent of x is not itself then we have not yet find the root of the tree
    2. Travel up the tree by recursively calling the find function until we find the parent
2. Then create the union function
    1. First we find the root of y and the root of x and change parents of the trees

```python
# IF size is given
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        """Finds the root of the set that x belongs to, with path compression."""
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])  # Path compression
        return self.root[x]

    def union(self, x, y):
        """Unites the sets that x and y belong to, by rank."""
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        """Checks if x and y are in the same set."""
        return self.find(x) == self.find(y)
 
 # If size is not given:
 class UnionFind:
    def __init__(self):
    # IMPORTANT:
    # IMPORTANT:
    # IMPORTANT:
    # If we can guarantee that edges are unique and the connections are valid
    # Then we can use the length of edges + 1 in an array
        self.root = {}  # Maps an element to its parent
        self.rank = {}  # Maps an element to its rank

    def find(self, x):
        """Finds the root of the set that x belongs to, with path compression."""
        if x not in self.root:
            self.root[x] = x  # Initialize with itself as root
            self.rank[x] = 1  # Initialize rank
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])  # Path compression
        return self.root[x]

    def union(self, x, y):
        """Unites the sets that x and y belong to, by rank."""
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        """Checks if x and y are in the same set."""
        # Only check connection if both elements have been added
        if x in self.root and y in self.root:
            return self.find(x) == self.find(y)
        return False

```

## Example - Counting Connected Components (Leetcode 323)

```python
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size
    
    def find(self, x):
        """Finds the root of the set that x belongs to, with path compression."""
        # Return value if the node equals itself
        if self.parent[x] == x:
            return x
        # If node does not equal itself, recursively find the parent then compress the path
            # It will point the child directly to parent node instead of creating a linked list
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Connect the root to the greatest rank between the two roots
                # This also prevents a linked list from happening to the parent node
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
    

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unionFind = UnionFind(n)

        # Connect together the different roots based on edges
        for x, y in edges:
            unionFind.union(x, y)
        
        # Applying find to each node to ensure path compression
            # Creates a set of parent nodes so we can find the length of all parent nodes
            # This tells us the different groups of connections
        return len(set(unionFind.find(i) for i in range(n)))
```

## Example - Detecting a Cycle (Leetcode 684)

In the image below, (1, 5) edges will connect thus creating a cycle because they are in the same set.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/5b35dd2a-6547-46a4-92d8-708317b7c83e/Untitled.png)

```python
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
    
    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        # Cycle has been detected
            # When parent nodes equal each other it means the edge that we will connect will form a cycle
            # Due to nodes pointing to parent nodes to show which group the connection it is in
            # If they are in the same group, it means the edge we are connecting will form its own connection
            # Thus creating a loop
        if parentX == parentY:
            return False
        else:
            if self.rank[parentX] > self.rank[parentY]:
                self.parent[parentY] = parentX
            elif self.rank[parentX] < self.rank[parentY]:
                self.parent[parentX] = parentY
            else:
                self.parent[parentY] = parentX
                self.rank[parentX] += 1
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind()

        for x, y in edges:
            if not uf.union(x,y):
                return [x,y]
        
        return []
```