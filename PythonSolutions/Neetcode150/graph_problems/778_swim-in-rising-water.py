class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # Keep track of max height (current time)
            # We use the height as time when traversing since: time == height we can traverse to
            # Due to the water rising based on time: e.g. height 2 means we waited a time of 2 for water to rise
        maxHeight = grid[0][0] # Current max height (& time) is the start point

        # Min heap so that we can select the smallest height to traverse to for each direction
        minHeap = [(maxHeight, 0, 0)] # (maxHeight/Time, row, col)

        visited = set()
        # Heap BFS traversal 
        while minHeap:
            # Pop smallest time within heap so we find the SHORTEST path
                # Height becomes the time since: time == height we can traverse to
            currMaxTime, row, col = heapq.heappop(minHeap)

            # Solved case: Return max time/height traversed to when we hit the end bottom right corner (last row, last col)
            if row == ROWS - 1 and col == COLS - 1:
                return currMaxTime

            for dx, dy in DIRS:
                newRow, newCol = row+dx, col+dy

                # *Do checks right away BEFORE traversing to the cells*
                    # Prevents adding the wrong cell to visited after popping heap

                # Base case 1: Out of bounds
                if newRow > ROWS - 1 or newCol > COLS - 1 or newRow < 0 or newCol < 0:
                    continue
                
                # Base case 2: Cell has been visited
                if (newRow, newCol) in visited:
                    continue

                # Visit the cell
                visited.add((newRow, newCol))
                # Find the max time/height between current cell or new cell
                    # If we are on a larger height than other cells, we can traverse to those cells right away without waiting
                    # Therefore, it helps us keep track of the shortest time when the heap pops (thus finding shortest path)
                heapq.heappush(minHeap, (max(currMaxTime, grid[newRow][newCol]), newRow, newCol))
            
        return maxHeight