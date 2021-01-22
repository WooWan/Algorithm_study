n = 12
m = 6
square = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
	square[i] = list(map(str, input()))


result = 0
colors = ['R', 'G', 'B', 'P', 'Y']
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

result = 0
cnt = 0


def dfs(color, x, y):
	global cnt
	cnt += 1
	visited[x][y] = True
	for i in range(4):
		nx = x+dx[i]
		ny = y + dy[i]
		if 0 <= nx < n and 0 <= ny < m:
			if square[nx][ny] == color and not visited[nx][ny]:
				dfs(color, nx, ny)

#n이 4이상이라면 해당 값들 모두 None처리!


def bomb(color, x, y):
	square[x][y] = None
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0 <= nx < n and 0 <= ny < m:
			if square[nx][ny] == color and visited[nx][ny]:
				bomb(color, nx, ny)
#fall 1번 할떄마다 한칸씩 땡겨진다!!
#i랑 j를 바꿔줘서 열을 먼저 순회하게 바꿔주었다


def fall():
	for i in range(m):
		for j in range(n):
			if square[j][i] == None:
				for k in range(j, 0, -1):
					square[k][i] = square[k-1][i]
				square[0][i] = '.'


while True:
	check = False
	visited = [[False for _ in range(m)] for _ in range(n)]
	for i in range(n):
		for j in range(m):
			cnt = 0
			if square[i][j] != "." and not visited[i][j]:
				dfs(square[i][j], i, j)
				if cnt >= 4:
					check = True
					bomb(square[i][j], i, j)
					fall()
	if check:
		result += 1
	else:
		break


print(result)
