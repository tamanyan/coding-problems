from typing import List


class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.options = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        answer = 0

        for nx in range(0, len(grid)):
            for ny in range(0, len(grid[nx])):
                self.size = 0
                self.dfs(grid, nx, ny, 0, 0)
                answer = max(self.size, answer)
                # print(answer)
        # return self.dfs(grid, 0, 0)
        
        return answer

    def isInvalid(self, grid: List[List[int]], nx: int, ny: int) -> bool:
        if not (nx < len(grid) and ny < len(grid[nx])) or (nx < 0 or ny < 0):
            return True
        else:
            return False
    
    def dfs(self, grid: List[List[int]], nx: int, ny: int, prev_x: int, prev_y: int):
        if self.isInvalid(grid, nx, ny):
            return 0
        
        if grid[nx][ny] == 0:
            return 0

        # print("onprocess", "x:", nx + 1, "y:", ny + 1, grid[nx][ny])
        grid[nx][ny] = 0
        self.size += 1

        for pair in self.options:
            next_x = nx + pair[0]
            next_y = ny + pair[1]

            if next_x == prev_x and next_y == prev_y:
                continue

            self.dfs(grid, next_x, next_y, nx, ny)
        
        return 1