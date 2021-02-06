import sys
#음 아직 python 문법도 익숙치 않고, bfs dfs 개념도 살짝 헷갈렸다
#모든 칸의 경우의 수를 모두 탐색해야하므로 visit처리 주의하기!
#dfs,bfs로는 손가락 욕 모양같은 아름다음 모양을 표현할 수 없다
#pypy에서는 시간 초과가 뜨지않는데 파이썬은 시간초과 느리다 파이썬 !
n, m = map(int, input().split(' '))
paper = list()
for i in range(n):
	paper.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

max_sum = 0


def poly(sum, x, y, cnt, visited):
	global max_sum
	if cnt == 0:
		max_sum = max(max_sum, sum)
		return
	sum += paper[x][y]
	for i in range(4):
		nx = x+dx[i]
		ny = y+dy[i]
		if 0 <= nx < n and 0 <= ny < m:
			if not visited[nx][ny]:
				visited[nx][ny] = True
				poly(sum, nx, ny, cnt-1, visited)
				visited[nx][ny] = False
	return sum


def siba(x, y):
	#손가락 욕모양 ^^,,,ㅎㅎ
	result = 0
	#ㅗ
	if x >= 0 and x < n-1 and y >= 1 and y < m-1:
		result = max(result, paper[x][y] + paper[x][y-1]+paper[x][y+1]+paper[x+1][y])
	#ㅏ
	if x >= 1 and x < n-1 and y >= 0 and y < m-1:
		result = max(result, paper[x][y] + paper[x+1][y]+paper[x-1][y]+paper[x][y+1])
	#ㅜ
	if x >= 1 and x < n and y >= 1 and y < m-1:
		result = max(result, paper[x][y]+paper[x][y+1]+paper[x][y-1]+paper[x-1][y])
	#ㅓ
	if x >= 1 and x < n-1 and y >= 1 and y < m:
		result = max(result, paper[x][y] + paper[x-1]
		             [y] + paper[x+1][y]+paper[x][y-1])
	return result


visited = [[False for _ in range(m)] for _ in range(n)]
temp = 0
for i in range(n):
	for j in range(m):
		# visited = [[False for _ in range(m)] for _ in range(n)]
		visited[i][j] = True
		max_sum = max(poly(0, i, j, 4, visited), max_sum)
		visited[i][j] = False
		# visited = [[False for _ in range(m)] for _ in range(n)]
		max_sum = max(siba(i, j), max_sum)
print(max_sum)
