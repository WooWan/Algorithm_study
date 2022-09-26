from typing import List


class Solution:
    grid: List[List[str]]

    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(x: int, y: int):
            for dx, dy in (1, 0), (0, -1), (-1, 0), (0, 1):
                nx = x + dx
                ny = y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny] == "1":
                        grid[nx][ny] = "0"
                        dfs(nx, ny)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count


sol = Solution()

print(sol.numIslands([["1", "1", "1", "1", "0"],
                      ["1", "1", "0", "1", "0"],
                      ["1", "1", "0", "0", "0"],
                      ["0", "0", "0", "0", "0"]]))
