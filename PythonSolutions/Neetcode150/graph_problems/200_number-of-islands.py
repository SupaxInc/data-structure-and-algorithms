class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                # "Sink" the island so that its easier to count the islands
                if grid[row][col] == "1":
                    self.dfs(grid, row, col)
                    count += 1
        
        return count
    
    def dfs(self, grid, row, col):
        # Check if the cell were on is valid
        if row < 0 or col < 0 or row > len(grid)-1 or col > len(grid[0])-1 or grid[row][col] == "0":
            return
        
        # Visit the cell
        grid[row][col] = "0"

        # Traverse the cell in four directions
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col - 1)
        