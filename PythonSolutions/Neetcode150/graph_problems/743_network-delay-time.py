class DjikstraSolution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create the directed graph using the edge (times) list
        graph = defaultdict(list)
        for source, target, time in times:
            graph[source].append((target, time)) # Node: Time
        
        # Create the distance times list for all nodes in the graph
            # 1 to n + 1, since nodes begin at 1 and not 0
        vertexTimes = {node: float("inf") for node in range(1, n+1)}
        vertexTimes[k] = 0 # Set the source node with time of 0

        # Create a minheap and add source as first in the heap
        minHeap = [(0, k)] # Weight, Node (weight is first so it can be used as the sorted value)

        visited = set()
        while minHeap:
            currTime, currNode = heapq.heappop(minHeap)

            # Skip if the node has already been visited
                # - Remember that popping a heap has randomized values so we may end up with a visited node
            if currNode in visited:
                continue
            
            # Visit the node
            visited.add(currNode)
            
            # Explore the neighbors for current node
            for neiNode, neiTime in graph[currNode]:
                newTime = neiTime + currTime

                # Only add to heap if new time is less than the neighbors previous time
                if newTime < vertexTimes[neiNode]:
                    vertexTimes[neiNode] = newTime
                    heapq.heappush(minHeap, (newTime, neiNode))
        
        # Get the max time amongst all times which is the min time we were able to reach the nodes
        maxTime = max(vertexTimes.values())

        # Return max time if we were able to reach all nodes else -1
        return maxTime if maxTime < float("inf") else -1

class BellmanFordSolution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create the distances list of size n + 1 with infinity except for source k
            # n + 1 size since the times are 1-based index
        distances = [float("inf")] * (n + 1)
        distances[k] = 0 # Source begins at distance of 0 since we are starting here

        # Relax the edges n - 1 times
        for _ in range(n - 1):
            # Used for early optimization to check if any edges were relaxed
            updated = False

            # Go through all edges (times)
            for source, target, weight in times:
                # Relax the edge if:
                    # - We have already found a path to the current source (not infinity)
                    # - The path from source to target is smaller than the current target's distance
                if distances[source] != float("inf") and distances[source] + weight < distances[target]:
                    distances[target] = distances[source] + weight
                    updated = True
            
            # If no edges were relaxed, stop for early optimization
            if not updated:
                break

        # Find the max time (distance) to reach a node as that will be the min time that all nodes received the signal
            # Ignore the 0th index since we did not use it (array size was n + 1 since times did not use node 0)
        maxTime = max(distances[1:]) 

        # If a node still contains an infinity distance then all nodes were not able to be reached
        return maxTime if maxTime < float("inf") else -1
