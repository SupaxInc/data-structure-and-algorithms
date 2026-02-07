from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.ROWS, self.COLS = len(heights), len(heights[0])
        self.DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.heights = heights
        
        pacific: set[tuple[int, int]] = set()
        atlantic: set[tuple[int, int]] = set()
        
        # Multi-source DFS below: Edges are adjacent to ocean so these cells can already go to that specific ocean

        # DFS through upper pacific and lower atlantic oceans
        for col in range(self.COLS):
            self.dfs(0, col, pacific)
            self.dfs(self.ROWS - 1, col, atlantic)

        # DFS through left pacific and right atlantic oceans
        for row in range(self.ROWS):
            self.dfs(row, 0, pacific)
            self.dfs(row, self.COLS - 1, atlantic)

        res = []
        # Intersection between pacific and atlantic oceans to see which cell can leak to both oceans
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])
        
        return res
    
    def dfs(self, row, col, ocean):
        # Base case 1: We have already traversed here previously in another DFS so skip
            # We do not need to do another DFS in a traversed cell since we already know at that point if water can flow
        if (row, col) in ocean:
            return
        
        # Mark that the water can flow to the ocean
        ocean.add((row, col))
        
        for dx, dy in self.DIRS:
            nr, nc = row + dx, col + dy

            if nr < 0 or nc < 0 or nr > self.ROWS - 1 or nc > self.COLS - 1:
                continue
            
            # Only DFS the heights greater than current cell (we are following opposite of rain flow from cell)
            if self.heights[nr][nc] >= self.heights[row][col]:
                self.dfs(nr, nc, ocean)
        
        return