## What is it?

Bellman Ford’s is similar to Dijkstra’s algorithm, however, it is much more reliable to be used for graphs with negative weights. It is a **dynamic programming** problem where we try out all the solution and pick out the best one.

In Bellman Ford’s we need to **relax** all the edges. Imagine trying to find the cheapest way to travel across cities connected by roads with tolls. Relaxing an edge is like discovering a cheaper route to a city you want to visit by going through another city instead. If the route is cheaper, we update our travel plan.

## Time Complexity

O(|V| * |E| = O(n^2) if it is a non-complete graph.

For a complete graph where there is an edge for all vertices: O(n^3)

# How does it work?

**Relaxing an edge** involves checking if the current known distance to reach the end vertex of that edge can be reduced by going through the start vertex of the edge and then following that edge. If it can be improved, you update the distance to this lower value.

We need to relax the edges: `Total number of vertices - 1 = |V| - 1`   times. For the example below, it would be `|V| - 1 = 7 - 1 = 6 times` .

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/90a53532-d67f-4461-be43-75c84cb504fe/Untitled.png)

---

**Step 1) Initialize the distances.** Set the source vertex distance as 0 and other vertices as infinity.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/5fc86014-3c42-4f65-b774-393d76cc8b59/Untitled.png)

**Step 2) Relax the edges |V|-1 times PER ITERATION.** Update the distance to the target vertex if the sum of the distance to the source vertex and edge weight is less than the current distance to the target vertex. Only update the vertices if we know the distance, if its infinity skip it since we don’t know how to get there yet.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/cbc0591c-8f4a-499b-8a16-c2f1634bbee2/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/7301217e-177a-4525-801d-5d7c60f58f96/Untitled.png)

First iteration is finished.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/9c6cf9ef-b1ba-487a-9804-cff3d4ba305f/Untitled.png)

An example of the second iteration above where it ends up finding an edge to relax after the first iteration.

**Step 3) Negative cycle check.** Run the relaxation step one more time for each edge to check for negative cycles. If any distance is updated during this step, it means there's a negative weight cycle in the graph

**WATCH THE VIDEO BELOW TO SEE HOW IT ACTUALLY WORKS!**

https://www.youtube.com/watch?v=obWXjtg0L64

## Negative Weight Cycles

A negative weight cycle in a graph is a cycle whose total sum of edge weights is negative. In the context of shortest path algorithms, negative weight cycles have significant implications:

1. **Path Costs**: If a negative weight cycle is reachable from the source, it can cause the shortest path cost to be infinitely decreasing. For any vertex on the cycle, repeatedly traversing the cycle can reduce the path cost indefinitely.
2. **Shortest Path Algorithms**: Algorithms like Dijkstra's algorithm do not work correctly in graphs with negative weight edges, particularly if there are negative weight cycles. However, the Bellman-Ford algorithm can detect negative weight cycles and handle them appropriately.

Example:

```python
Consider a graph with vertices A, B, C, and D, 
and the following edges with their respective weights:

A -> B with weight 1
B -> C with weight -2
C -> D with weight 1
D -> B with weight 1

The cycle B -> C -> D -> B has a total weight of -2 + 1 + 1 = 0. 
If the weight of B -> C were -3, the total weight would be -3 + 1 + 1 = -1, 
forming a negative weight cycle.
```

# Template Code

```python
def bellman_ford(graph, num_vertices, start):
    # Initialize distances from start to all other vertices as infinity
    distances = [float('inf')] * num_vertices
    distances[start] = 0
    
    # Relax edges up to (num_vertices - 1) times
    for i in range(num_vertices - 1):
    
        # Flag to check if any distance was updated in this pass
        updated = False
        
        # Relaxing the edges here n-1 times per iteration
        for u, v, weight in graph:
		        # Skip if the source distance is infinity (don't know how to get there yet)
		        # If its known, then check if the current weight + source distance is smaller
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                updated = True
                
        # If no distances were updated, we can terminate early for optimization
        if not updated:
            break
    
    # Check for negative weight cycles by relaxing edges 1 last time
				    # When there has been no distances updated for awhile
				    # Or after n-1 times has finished
    for u, v, weight in graph:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            print("Graph contains a negative weight cycle")
            return None
    
    return distances

# Example usage
# Graph represented as a list of edges (u, v, weight)
edges = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]
num_vertices = 5
start_vertex = 0

shortest_paths = bellman_ford(edges, num_vertices, start_vertex)
print(shortest_paths)  # Output: [0, -1, 2, -2, 1]

```

# Examples

## Cheapest Flights Within K Stops

Debug code below to see how each iteration works for relaxing the edges. You can see if we don’t know the distance yet, it will not calculate the distance due to the previous stop we didn’t know how to get the target yet.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/f87cabf2-8d22-410c-bb4c-b00e5c7c3bac/5867b342-fa79-4f79-9a4d-5bf0deeeb3a1/Untitled.png)

```python
def findCheapestPrice(n, flights, src, dst, K):
    """
    Finds the cheapest price from src to dst with up to K stops.
    
    :param n: Number of nodes (cities).
    :param flights: List of flights represented as (source, destination, price).
    :param src: Source node.
    :param dst: Destination node.
    :param K: Maximum number of stops.
    :return: The cheapest price to get from src to dst with up to K stops. Returns -1 if not possible.
    """
    # Initialize distances with infinity
    distances = [[float('inf')] * n for _ in range(K + 2)]
    distances[0][src] = 0  # Distance to source from source is 0
    
    # Relax the edges K + 1 times to account for up to K stops
    for i in range(1, K + 2):
        distances[i][src] = 0  # Keep source at 0
        for u, v, w in flights:
            # If a cheaper price is found, update the distance
            distances[i][v] = min(distances[i][v], distances[i-1][u] + w)
    
    # The cheapest price after considering up to K stops
    cheapest_price = distances[K + 1][dst]
    return cheapest_price if cheapest_price != float('inf') else -1

# Example usage
if __name__ == "__main__":
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    K = 1
    
    result = findCheapestPrice(n, flights, src, dst, K)
    print(f"The cheapest price from {src} to {dst} with up to {K} stop(s) is: {result}")

```