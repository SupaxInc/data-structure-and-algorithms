class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countLetters = defaultdict(int)

        for task in tasks:
            # Decrement the counts to negatives since we need to create a max heap
            countLetters[task] -= 1
        
        # Max heap to keep track of the most frequent letters
        maxHeap = list(countLetters.values())
        heapq.heapify(maxHeap)

        # Queue to keep track of what task is next to execute
        queue = deque() # Pairs of [-count, idle time]
        time = 0

        # Begin executing the tasks
            # If the max heap is not empty then there are tasks no longer idle and ready to execute
            # If the queue is not empty then there are idle tasks cooling down
        while len(maxHeap) > 0 or len(queue) > 0:
            time += 1

            if len(maxHeap) > 0:
                # Execute the task and prepare to queue it to cool it down for next execution
                    # Incrementing the task to (remember max heaps are negatives) 
                    # Add cooldown time to know when its ready again
                task = [heapq.heappop(maxHeap)+1, time+n]
            
                # Add to queue if the SAME task is not yet 0 (still has more to execute)
                if task[0] < 0:
                    queue.append(task)
            
            if queue and len(queue) > 0:
                # Check if the first task in the queue is ready to be executed again
                # NOTE: There will never be two tasks ready at once since we only process 1 at a time
                if queue[0][1] == time:
                    # Add the task negative increment back to the heap for execution
                    heapq.heappush(maxHeap, queue.popleft()[0])
        
        return time