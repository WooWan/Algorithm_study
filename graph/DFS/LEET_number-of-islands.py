from typing import List


def numIslands( grid: List[List[str]]) -> int:
    count = 0

    def dfs(x,y):
        for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
            nx = x + dx
            ny = y + dy
            if 0<=nx<len(grid) and 0<=ny<len(grid[0]):
                if grid[nx][ny] == "1":
                    grid[nx][ny] = "0"
                    dfs(nx,ny)



    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(i,j)
            if grid[i][j] == "1":
                dfs(i,j)
                count += 1
    return count

grid =[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
grid = [["1"],["1"]]
print(numIslands(grid))

