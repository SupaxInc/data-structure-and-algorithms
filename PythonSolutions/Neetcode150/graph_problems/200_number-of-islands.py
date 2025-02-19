class DFSSolution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.ROWS, self.COLS = len(grid), len(grid[0])
        self.DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        count = 0

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.grid[row][col] == "1":
                    # Run a DFS once an island has been found, this will do a DFS on the entire island
                    # This "sinks" the entire island, so next loop iteration will not find anymore "1"s
                    self.dfs(row, col)

                    # Count this as 1 island after sinking the entire island
                    count += 1
        
        return count

    def dfs(self, row, col):
        # Base case 1: Boundary check
        if row > self.ROWS-1 or col > self.COLS-1 or row < 0 or col < 0:
            return
        
        # Base case 2: Visited check
        if self.grid[row][col] == "0":
            return
        
        # Visit the cell, "sink" a part of the island
        self.grid[row][col] = "0"

        for dx, dy in self.DIRS:
            # Continue to sink all of the islands that have not been visited yet
            self.dfs(row+dx, col+dy)

class BFSSolution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == "1":
                    self.bfs(grid, row, col)
                    count += 1
        
        return count
    
    def bfs(self, grid, startRow, startCol):
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        queue = deque([(startRow, startCol)])

        while queue:
            row, col = queue.popleft()

            if row < 0 or col < 0 or row > len(grid)-1 or col > len(grid[0])-1 or grid[row][col] == "0":
                continue
            
            grid[row][col] = "0"

            for rowDir, colDir in dirs:
                queue.append([row + rowDir, col + colDir])
                    