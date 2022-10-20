from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        grid: List[List[str]]

        def dfs(x: int, y: int):
            for dx, dy in (1, 0), (0, -1), (-1, 0), (0, 1):
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] != "1":
                    continue
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
