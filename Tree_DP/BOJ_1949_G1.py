#1949 우수마을(트리 dp)
#dp[x][0]= x포함, dp[x][1]= x미포함
#따라서 우수마을은 근접할 수 없기 때문에 보통마을인 +=dp[x][1], 보통마을은 보통마을 또는 우수마을과 근접할 수 있으므로
#max(dp[node][0], dp[node][1])

import sys
input= sys.stdin.readline
sys.setrecursionlimit(20000)

n= int(input())

population=[0]+list(map(int, input().split()))
dp=[[0]*2 for i in range(n+1)]
visited=[False]*(n+1)
tree=[[] for i in range(n+1)]
for i in range(n-1):
    a,b= map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(x):
    dp[x][0]=population[x]
    for node in tree[x]:
        if not visited[node]:
            visited[node]=True
            dfs(node)
            dp[x][0]+=dp[node][1]
            dp[x][1]+=max(dp[node][0], dp[node][1])

visited[1]=True
dfs(1)
print(max(dp[1][1], dp[1][0]))