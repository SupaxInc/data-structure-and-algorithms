class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        # Create a DIRECTED graph
        for source, target, weight in times:
            graph[source].append((target, weight))
        
        # Set the current distance of all vertices from 1 to n, and set distance as infinity since none has been found yet
            # This will be used to map the shortest path distance to the source
        vertexTimes = { vertex: float("inf") for vertex in range(1, n+1) }

        # Set the source node K, to 0 since time to a source would just be 0
        vertexTimes[k] = 0

        minHeap = [(0, k)] # (current time, current selected node)
        visited = set()

        while minHeap:
            currTime, currNode = heapq.heappop(minHeap)
            if currNode in visited: continue

            visited.add(currNode)

            for nei, time in graph[currNode]:
                newTime = currTime + time
                # Only store the new time that is shorter than current neighbors shortest time path
                if newTime < vertexTimes[nei]:
                    vertexTimes[nei] = newTime
                    heapq.heappush(minHeap, (newTime, nei))
        
        # The max time path is the answer
            # We are always looking for the shortest time path, and the max time path will give us the answer
            # To find that all nodes received the signal
        maxTime = max(vertexTimes.values())

        # If a nodes max time is infinity that means we weren't able to reach all nodes in time
        return maxTime if maxTime < float("inf") else -1

