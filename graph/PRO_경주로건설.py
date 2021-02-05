import heapq
INF = 1e9


def bfs(n, board):
    visited = [[False for _ in range(n)] for _ in range(n)]
    graph = [[[[INF]*2]*2 for _ in range(n)] for _ in range(n)]
    heap = list()
    heapq.heappush(heap, (0, 0, 0, 0, 0))
    visited[0][0] = True
    while heap:
        cnt, x, y, bx, by = heapq.heappop(heap)
        #이미 방문하였을경우 무시
        if x == n-1 and y == n-1:
            return graph[n-1][n-1]
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx = x+dx
            ny = y+dy
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] != 1:
                    # 같은 방향을 보고 있을 경우
                    if x == 0 and y == 0 or (bx == dx and by == dy):
                        if cnt+100 < graph[nx][ny][dx][dy]:
                            graph[nx][ny][dx][dy] = cnt+100
                            heapq.heappush(heap, (cnt+100, nx, ny, dx, dy))
                    else:
                        #다른 방향일 경우 꼭지점+ 직선 +=600
                        if cnt+600 < graph[nx][ny][dx][dy]:
                            graph[nx][ny][dx][dy] = cnt+600
                            heapq.heappush(heap, (cnt+600, nx, ny, dx, dy))


def solution(board):
    answer = INF
    n = len(board)
    graph = bfs(n, board)
    for i in range(2):
        for j in range(2):
            answer = min(answer, graph[i][j])
    return answer
