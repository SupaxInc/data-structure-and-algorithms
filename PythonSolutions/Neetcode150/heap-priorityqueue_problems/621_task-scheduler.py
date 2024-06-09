class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countLetters = defaultdict(int)

        for c in tasks: # O(26)
            countLetters[c] -= 1 # Negative so we can turn min heap to max heap

        # Max heap allows us to fill the CPU with the most frequent tasks first
        # Helps with the least amount of time waiting as we can fill other tasks in between waiting for most frequent to be ready
        maxHeap = list(countLetters.values())
        heapq.heapify(maxHeap)
        
        time = 0
        # We need a queue to know which tasks are ready to be executed again
        queue = deque() # Pairs of [-count, idleTime]
        while len(maxHeap) > 0 or len(queue) > 0:
            time += 1

            if len(maxHeap) > 0:
                # Grab the most frequent task and decrement it (executes the task)
                # Add the idle time to check when we can run the task again
                task = [heapq.heappop(maxHeap)+1, time+n] # O(26 log 26)

                # Add to queue if there are more of the same tasks to execute
                if task[0] < 0:
                    queue.append(task)

            # Push to heap if the next tasks idle time is done and is ready to be executed again
            if queue and queue[0][1] == time: # O(26 log 26)
                heapq.heappush(maxHeap, queue.popleft()[0])
        
        return time

