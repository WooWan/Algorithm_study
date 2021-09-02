# g3 저울 최단 거리로 이어져 있지 않다면, 비교를 할 수 없는 정점

import sys
input = sys.stdin.readline
n=int(input())
m= int(input())
INF=int(1e9)

graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b= map(int, sys.stdin.readline().split())
    graph[a][b]=1

for i in range(1,n+1):
    graph[i][i]=0

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])

for i in range(1,n+1):
    answer=0
    for j in range(1,n+1):
        if graph[i][j]==INF and graph[j][i]==INF: answer+=1
    print(answer)