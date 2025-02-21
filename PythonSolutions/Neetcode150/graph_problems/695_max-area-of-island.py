class DFSSolution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.ROWS, self.COLS = len(grid), len(grid[0])
        self.DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        maxArea = 0

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.grid[row][col] == 1:
                    maxArea = max(maxArea, self.dfs(row, col))
        
        return maxArea

    def dfs(self, row, col):
        # Base case 1: Boundary check
        if row > self.ROWS-1 or col > self.COLS-1 or row < 0 or col < 0:
            # Returns 0 as its not a valid area
            return 0
        
        # Base case 2: Visited check
        if self.grid[row][col] == 0:
            # Returns 0 as its not a valid area
            return 0
        
        # Visit the cell
        self.grid[row][col] = 0 # "Sink" the island and leave it as 0 so we don't end up calling more DFS later on the same island
        totalArea = 1 # The total area for current cell is just a 1

        for dx, dy in self.DIRS:
            # Explore the four directions and add the total area of them
            totalArea += self.dfs(row+dx, col+dy)
        
        # Finally, return the last summed total area of all traveled cells
        return totalArea
        
class BFSSolution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.ROWS, self.COLS = len(grid), len(grid[0])
        self.DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        maxArea = 0

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.grid[row][col] == 1:
                    maxArea = max(maxArea, self.bfs(row, col))
        
        return maxArea

    def bfs(self, row, col):
        queue = deque([(row, col)])

        totalArea = 0
        while queue:
            row, col = queue.popleft()

            # Base case 1: Boundary check
            if row > self.ROWS-1 or col > self.COLS-1 or row < 0 or col < 0:
                continue
            
            # Base case 2: Visited check
            if self.grid[row][col] == 0:
                continue
            
            # Visit the cell
            self.grid[row][col] = 0
            totalArea += 1 # Add the total area as its iterative compared to DFS

            # Explore the four directions
            for dx, dy in self.DIRS:
                queue.append((row+dx, col+dy))
        
        return totalArea
        
