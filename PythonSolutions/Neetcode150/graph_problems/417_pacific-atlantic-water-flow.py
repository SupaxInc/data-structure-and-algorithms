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