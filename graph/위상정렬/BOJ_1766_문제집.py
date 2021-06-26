#1766 문제집
#1번~n번중에 queue대신 heap을 쓰면 풀 수 있을 것같다..

import heapq
import sys

input=sys.stdin.readline

n,m=map(int, input().split())
indegree=[0]*(n+1)
heap=[]
graph=[[] for i in range(n+1)]
for i in range(m):
    a,b= map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1

for i in range(1,n+1):
    if indegree[i]==0: heapq.heappush(heap,i)

while heap:
    x=heapq.heappop(heap)
    for j in graph[x]:
        indegree[j]-=1
        if indegree[j]==0:
            heapq.heappush(heap, j)

    print(x, end=' ')