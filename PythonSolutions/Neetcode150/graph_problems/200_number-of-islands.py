class DFSSolution(object):
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
                    