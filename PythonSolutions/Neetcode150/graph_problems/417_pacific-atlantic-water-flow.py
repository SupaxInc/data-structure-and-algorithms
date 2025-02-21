class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.heights = heights
        self.ROWS, self.COLS = len(heights), len(heights[0])
        self.DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        pacific = set()
        atlantic = set()
        res = []

        # Run the DFS on left and right boundaries to mark which cells we can visit based on inner water flow
        for row in range(self.ROWS):
            self.dfs(row, 0, pacific, self.heights[row][0])
            self.dfs(row, self.COLS-1, atlantic, self.heights[row][self.COLS-1])
        
        # Run the DFS on the top and bottom boundaries
        for col in range(self.COLS):
            self.dfs(0, col, pacific, self.heights[0][col])
            self.dfs(self.ROWS-1, col, atlantic, self.heights[self.ROWS-1][col])
        
        # Find the intersection of which cells we were able to visit based on water flow for both pacific and atlantic
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])
        
        return res
    
    def dfs(self, row, col, visited, prevHeight):
        # Base case 1: Boundary check
        if row > self.ROWS-1 or col > self.COLS-1 or row < 0 or col < 0:
            return
        
        # Base case 2: 
            # - Visited check 
            # - Check if current land height is larger than previous land height, water can't flow
        if self.heights[row][col] < prevHeight or (row, col) in visited:
            return
        
        # Visit the cell
        visited.add((row, col))
        prevHeight = self.heights[row][col]

        for dx, dy in self.DIRS:
            self.dfs(row+dx, col+dy, visited, prevHeight)
        
        return