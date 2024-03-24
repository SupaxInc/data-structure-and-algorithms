class DFSSolution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == 1:
                    area = self.dfs(grid, row, col, 0)
                    maxArea = max(maxArea, area)
        
        return maxArea

    def dfs(self, grid, row, col, area):
        if row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[row]) - 1:
            return 0
        if grid[row][col] == 0:
            return 0
        
        grid[row][col] = 0
        area = 1
        area += self.dfs(grid, row + 1, col, area)
        area += self.dfs(grid, row, col + 1, area)
        area += self.dfs(grid, row - 1, col, area)
        area += self.dfs(grid, row, col - 1, area)

        return area
        
class BFSSolution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        for row in range(0, len(grid)):
            for col in range(0, len(grid[row])):
                if grid[row][col] == 1:
                    maxArea = max(self.bfs(grid, row, col), maxArea)
        
        return maxArea

    def bfs(self, grid, startRow, startCol):
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        area = 0
        
        queue = deque([(startRow, startCol)])
        while queue:
            row, col = queue.popleft()

            if row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[row]) - 1:
                continue

            if grid[row][col] == 0:
                continue

            area += 1
            grid[row][col] = 0
            
            for rowDir, colDir in DIRS:
                queue.append([row + rowDir, col + colDir])
        
        return area
        
