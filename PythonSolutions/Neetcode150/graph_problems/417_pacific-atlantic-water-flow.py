class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.ROWS, self.COLS = len(heights), len(heights[0])
        res = []

        pacific = set()
        atlantic = set()

        # Mark starting from the left and right boundaries
        for row in range(0, self.ROWS):
            self.dfs(heights, row, 0, pacific, heights[row][0]) # Left boundary is pacific
            self.dfs(heights, row, self.COLS - 1, atlantic, heights[row][self.COLS-1]) # Right boundary is atlantic
        
        # Mark starting from the top and bottom boundaries
        for col in range(0, self.COLS):
            self.dfs(heights, 0, col, pacific, heights[0][col]) # Top boundary is pacific
            self.dfs(heights, self.ROWS - 1, col, atlantic, heights[self.ROWS-1][col]) # Bottom boundary is atlantic
        
        # Check for intersections between atlantic and pacific water flows
        for row in range(0, self.ROWS):
            for col in range(0, self.COLS):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])
        
        return res

    
    def dfs(self, heights, row, col, visited, prevHeight):
        if row < 0 or col < 0 or row > self.ROWS - 1 or col > self.COLS - 1:
            return 
        
        if heights[row][col] < prevHeight or (row, col) in visited:
            return
        
        visited.add((row, col))
        prevHeight = heights[row][col]
        
        self.dfs(heights, row + 1, col, visited, prevHeight)
        self.dfs(heights, row, col + 1, visited, prevHeight)
        self.dfs(heights, row - 1, col, visited, prevHeight)
        self.dfs(heights, row, col - 1, visited, prevHeight)

        return
    
class Solution2:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.ROWS, self.COLS = len(heights), len(heights[0])
        self.heights = heights
        self.DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        pacific = set()
        atlantic = set()
        res = []

        # Begin at the left and right boundaries
            # Boundaries lets us know that it can already flow to that part of the ocean
        for row in range(self.ROWS):
            self.dfs(row, 0, pacific, self.heights[row][0]) 
            self.dfs(row, self.COLS - 1, atlantic, self.heights[row][self.COLS-1])
        
        # Begin at top and bottom boundaries
        for col in range(self.COLS):
            self.dfs(0, col, pacific, self.heights[0][col])
            self.dfs(self.ROWS - 1, col, atlantic, self.heights[self.ROWS-1][col])
        
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])
        
        return res

    def dfs(self, row, col, visited, prevHeight):
        # Boundary check
        if row > self.ROWS - 1 or col > self.COLS - 1 or row < 0 or col < 0:
            return
        
        # Valid check
        if (row, col) in visited or prevHeight > self.heights[row][col]:
            return
        
        visited.add((row, col))
        for dx, dy in self.DIRS:
            self.dfs(row+dx, col+dy, visited, self.heights[row][col])

        return