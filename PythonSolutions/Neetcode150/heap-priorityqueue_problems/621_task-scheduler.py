from collections import defaultdict, heapq, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqTask = defaultdict(int)
        maxHeap = []

        for task in tasks:
            freqTask[task] -= 1

        # Heapify frequence of tasks so we always use the task thats highest
            # If we don't we will end up waiting longer since we can't execute same tasks per interval
        maxHeap = list(freqTask.values())
        heapq.heapify(maxHeap)

        # Use a queue to check when a next time is ready by the next idle time
        queue: tuple(int, int) = deque()

        t = 0
        while maxHeap or queue:
            t += 1
            # There is a task ready for execution
            if len(maxHeap) > 0:
                task = heapq.heappop(maxHeap)
                newTask = task + 1

                if newTask != 0:
                    queue.append((newTask, t + n))
            
            # A task's idle time is complete and is ready for execution
            if queue and queue[0][1] == t:
                task = queue.popleft()[0]

                heapq.heappush(maxHeap, task)

        return t