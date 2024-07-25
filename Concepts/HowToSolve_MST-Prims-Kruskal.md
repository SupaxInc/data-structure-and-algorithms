# What is a Minimum Spanning Tree?

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/4e30c958-3e10-415f-8ba4-bd13e0f62dd3/Untitled.png)

- A span tree is a sub-graph of a graph that takes all vertices but only n-1 edges
    - See example picture above, total number of 6 vertices and 5 edges.
    S = (V, E)
    V = V
    |E| = |V| - 1
    - Since we removed 1 edge, it no longer has a cycle (trees do not have cycles)
    - **You can choose any edges to leave out**
        - This means we can have 6 different spanning trees based on graph above

## How about a weighted graph?

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/a9267e59-39d2-4cd4-8938-cac14757d44f/Untitled.png)

- Using our equation:
Spanning tree = (V, E)
V = 4
|E| = |V| - 1 = 3
- We can have 3 edges for the weight graph above to create a spanning tree
- Based on the different combinations of the spanning tree, we are able to get the cost of each spanning tree

# How do we get the minimum cost of spanning trees?

We create all possibilities of spanning trees then grab the one with minimum cost.

**Is there a greedier method so we don’t have to try out all possibilities?** Yes, there are two algorithms that helps us follow a procedure in which it allows us to find the minimum cost of a spanning tree.

## Prim’s Algorithm

**Uses a BFS with a priority queue (heap)**

How it works:

- Initially, select a minimum weight edge from a graph. 10 is selected.
    - Usually this is an **arbitrary point** (random choice), we can select any known starting point.
    - Starting at the first point, lets say in a graph is usually (0, 0). This is a common strategy for Prims algorithm.
        - **It helps ensure that the MST construction begins with a known point and a cost of 0**

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/96ec3627-d98c-4175-8b3b-2b6e4593db63/Untitled.png)

- Continuously select the most minimum weight BUT we can only select the edges based on the vertices we have.
    - In the example above, we can only select edges that connect to 1 and 6.
- We can see that between 1 and 6, 1 has an edge with weight of 28 and 6 has an edge with weight of 25. Therefore, 25 is smaller.
    - Continuously repeat this until 6 edges.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/b179e05f-7436-4ab9-b11a-293c2df26c85/Untitled.png)

- The minimum spanning tree should now look like the graph below. From each vertices selected, we always selected the most minimum edge and continued from there to create 6 edges. (|V| = 7, |V| - 1 = 6 total edges)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/1c85098b-8775-42e5-8061-11172bdf4587/Untitled.png)

- The cost of the tree above would be 99.

**NOTE:** This algorithm does not work if the graphs are not connected to each other. If there are multiple groups of graphs and they are not connected, it won’t be possible.

### Time Complexity

O(E+VlogV) with a priority queue

### Template Code

Prim's algorithm begins with an **arbitrary vertex** and grows the spanning tree by adding the smallest edge that connects a vertex in the tree to a vertex outside it. This process repeats until all vertices are included in the tree.

Arbitrary vertex start point of (0,0) is usually selected for Prims algorithm as a common strategy, **It helps ensure that the MST construction begins with a known point and a cost of 0.**

In the example below, we are using the most minimum weight instead.

```python
import heapq

def prim(graph, start):
    # Assume graph is in adjacency list format: {node: [(weight, neighbor), ...]}
    visited = set([start])
    edges = [(weight, start, to) for weight, to in graph[start]]
    heapq.heapify(edges)
    minimum_cost = 0

    while edges:
        weight, frm, to = heapq.heappop(edges)
        
        # Undirected graph so there is chance we have already visited a point
                # This is needed since we are popping from a min heap
                # That means it will select the minimum cost edge
                # We may end up popping an edge we have already visited 
                # since its randomized based on min cost
        if to in visited:
	        continue
	       
        visited.add(to)
        minimum_cost += weight
        for next_edge in graph[to]:
            if next_edge[1] not in visited:
                heapq.heappush(edges, (next_edge[0], to, next_edge[1]))

    return minimum_cost

```

See [1584 - Min Cost to Connect All Points (Advanced)](https://www.notion.so/1584-Min-Cost-to-Connect-All-Points-Advanced-04e3b05b411144b292980e5f87e8dcfc?pvs=21) for another example.

---

## Kruskal’s Algorithm

This algorithm is another **greedy** method. 

How it works:

- Always select the minimum weight edge.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/ec5b5870-e74b-403b-aac5-bd0b0c98fd44/Untitled.png)

- Compared to Prim’s algorithm, we don’t care if its connected to the previous vertices we have selected.
    - So just select it even if vertices are not connected to each other
- If we start forming a cycle, do NOT include it in the solution. Discard the edge and choose another minimum weighted edge.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/5e01b1cd-0e3b-4c6b-975e-deedbaadf773/Untitled.png)

- In the picture above, you can see that it created the same tree as Prim’s algorithm.

### Time Complexity

**O(|V| * |E|) = O(n^2)**

- It is O(n^2) since we are always looking for the most minimum weight in the entire tree
- This can be improved sorting weighted edges first and union find
    - We can keep all of the edges in this sort and keep grabbing the most minimum weight.
    - This improves it to **O(E*logE)**

### Template Code

Start by sorting all the edges in the graph in non-decreasing order of their weight. Then, iterate over these edges, adding each edge to the spanning tree if it doesn't form a cycle, until you have*V*−1 edges in the tree or you've gone through all edges, where *V* is the number of vertices.

```python
class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def kruskal(edges, V):
    uf = UnionFind(V)
    minimum_cost = 0
    edges.sort(key=lambda x: x[2])  # Edge format: (u, v, weight)

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            minimum_cost += weight

    return minimum_cost

```

### Example Problem - Leetcode 1584

```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]
    
    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            # Union by rank
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1
            return True
        return False

class UnionFindSolution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        totalVertices = len(points)
        edges = []

        # Generate all possible edges with their weights (Manhattan distances)
        for i in range(totalVertices):
            for j in range(i + 1, totalVertices):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((weight, i, j))

        # Sort edges by weight
          # Allows us to select and connect the most minimum weights first for each point
        edges.sort()

        # Kruskal's algorithm to form MST
        uf = UnionFind(totalVertices)
        mst_cost = 0  # Total cost of the MST
        edges_used = 0  # Number of edges added to the MST

        for weight, u, v in edges:
            # Add edges 1 by 1, connecting points (u, v) together to form a graph
                # Check if it doesn't form a cycle
            if uf.union(u, v):  
                mst_cost += weight  # Add the edge's weight to the total cost
                edges_used += 1  # Increment the count of edges used in the MST

                # If we've used enough edges to form a MST (Edges = Vertices - 1)
                if edges_used == totalVertices - 1:  
                    break  # Exit the loop early

        return mst_cost
```

# When to use it?

- Use MST algorithms when you need to connect all points (nodes) in a graph with the minimum total edge weight without forming cycles.
    - Choose Prim's algorithm for dense graphs and when you have a good starting point
    - Choose Kruskal's algorithm for sparse graphs and when dealing primarily with edge lists.

# What algorithm is more effective?

**Efficiency of Prim's Algorithm**

- **Graph Density**: Prim's algorithm can be more efficient for dense graphs. In a dense graph, the number of edges is close to the maximum possible, which is *O*(n^2) for a graph with *N* vertices. Since Prim's algorithm updates the distances to the nearest unvisited vertex dynamically, it can handle dense graphs efficiently, especially when implemented with a min heap/priority queue. 
The priority queue ensures that the edge with the minimum weight is always selected next, without needing to sort all edges upfront.

```python
A --- B --- D
|  /  |  /  |
| /   | /   |
C --- E --- A

A dense graph is one where the number of edges is 
close to the maximum number of possible edges. 

In other words, almost every vertex is connected to almost every other vertex.
```

- **Edge Weights**: Prim's algorithm is efficient in handling situations where edge weights are updated or when the graph is not fully known upfront. It dynamically selects the next best edge to add to the MST, making it suitable for scenarios where the graph might change or when the full graph is not available from the beginning.

---

**Scenarios Where Kruskal's Might Be More Effective**

- **Sparse Graphs**: Kruskal's algorithm can be more effective for sparse graphs, where the number of edges is much less than the maximum possible. Since Kruskal's algorithm sorts all edges upfront and then iteratively adds the shortest edge that does not form a cycle, it can be efficient when the total number of edges is relatively low, leading to lower sorting costs.

```python
A --- B
|   
|   
C    D --- E
```

- **Simpler Union-Find Operations**: Kruskal's algorithm makes use of the Union-Find data structure to detect cycles. This approach can be more straightforward and require less overhead in scenarios where maintaining a priority queue (as in Prim's) is not as cost-effective. Especially in very sparse graphs, the simplicity of Union-Find operations can make Kruskal's algorithm faster.
- **Edge Cases**: In cases where the graph’s edges have unique weights, Kruskal's algorithm can be particularly straightforward since each edge decision is independent of the graph's structure. This can simplify the MST construction process.