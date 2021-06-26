#1005 ACM Craft
import sys
from collections import deque

input=sys.stdin.readline
queue=deque()
INF=-int(1e9)
t= int(input())
for test in range(t):
    n,k= map(int,input().split())
    arr=[0]+list(map(int,input().split()))
    dp=[INF]*(n+1)
    indegree=[0]*(n+1)
    graph=[[] for i in range(n+1)]
    for i in range(k):
        a,b= map(int, input().split())
        graph[a].append(b)
        indegree[b]+=1
    goal=int(input())
    for i in range(1,n+1):
        if indegree[i]==0:
            queue.append(i)
            dp[i]=arr[i]
    while queue:
        x= queue.popleft()
        for j in graph[x]:
            indegree[j]-=1
            dp[j] = max(dp[j], dp[x] + arr[j])
            if indegree[j]==0:
                queue.append(j)
    print(dp[goal])

