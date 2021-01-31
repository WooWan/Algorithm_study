import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
visited= [[False for _ in range(m)] for _ in range(n)]
arr=[list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]


max_arr=0
for i in range(1,n):
	for j in range(1,m):
		if arr[i][j]!=0: 
			arr[i][j]=min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1])+1

for i in range(n):
	for j in range(m):
		max_arr=max(max_arr,arr[i][j])
print(max_arr*max_arr)

