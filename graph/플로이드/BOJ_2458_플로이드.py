#플로이드 와샬 문제의 기본 아이디어는 경유이다. graph[a][b], graph[a][k]+graph[k][b]의 비교를 통해 그래프의 최소경로를 알아낼 수 있다
#이를 통해 문제에서 그래프 a,b가 연결되어있는지 비교를 할 수 있다

import sys

n,m = map(int,input().split())
INF=int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1, n+1):
        if i==j: graph[i][j]=1

for i in range(m):
    a,b=map(int, sys.stdin.readline().split())
    graph[a][b]=1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):
            graph[a][b]=min(graph[a][b], graph[a][k]+graph[k][b])
answer=n
for i in range(1,n+1):
    for j in range(1,n+1):
        #비교를 하려면
        if graph[i][j]==INF and graph[j][i]==INF:
            answer-=1
            break
print(answer)