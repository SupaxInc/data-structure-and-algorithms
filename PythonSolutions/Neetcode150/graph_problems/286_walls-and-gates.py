from collections.abc import Deque
from collections import deque
from typing import List
class Solution:
    # *Don't have premium leetcode so this is using Islands and Treasure from Neetcode: https://neetcode.io/problems/islands-and-treasure*
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.grid = grid
        self.ROWS, self.COLS = len(grid), len(grid[0])
        self.DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.INF = 2147483647

        self.queue: Deque[tuple[int, int]] = deque()

        # Multi-source BFS: Load all treasure chests up-front
        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.grid[row][col] == 0:
                    self.queue.append((row, col))
        
        # Run the level order BFS across all treasure chests
        self.levelOrderBFS()
    
    def levelOrderBFS(self):
        while self.queue:
            levelSize = len(self.queue)
            
            for _ in range(levelSize):
                r, c = self.queue.popleft()

                # Iterate through the new rows right away since current cell (treasure chest) is not important
                for dx, dy in self.DIRS:
                    nr, nc = r + dx, c + dy

                    if nr < 0 or nc < 0 or nr > self.ROWS - 1 or nc > self.COLS - 1:
                        continue
                    
                    # No need for a visited set since change INF values to a distance effectively "visiting" the cell
                    if self.grid[nr][nc] != self.INF:
                        continue
                    
                    # Add the distance by incrementing PREVIOUS popped row and col value
                    self.grid[nr][nc] = self.grid[r][c] + 1

                    self.queue.append((nr, nc))


#! Single Source BFS
class BruteForceSolution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.ROWS, self.COLS = len(grid), len(grid[0])
        self.DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        self.grid = grid

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if (self.grid[row][col] == 2147483647):
                    self.bfs(row, col)
    
    def bfs(self, row, col) -> None:
        queue = deque([(row, col)])

        dist = 0
        visited = set()
        while queue:
            levelSize = len(queue)
            dist += 1

            for _ in range(levelSize):
                r, c = queue.popleft()

                for dx, dy in self.DIRS:
                    nr, nc = r + dx, c + dy

                    if nr < 0 or nc < 0 or nr > self.ROWS - 1 or nc > self.COLS - 1:
                        continue
                
                    if self.grid[nr][nc] == -1 or (nr, nc) in visited:
                        continue

                    if self.grid[nr][nc] == 0:
                        self.grid[row][col] = dist
                        return
                
                    visited.add((nr, nc))

                    queue.append((nr, nc))