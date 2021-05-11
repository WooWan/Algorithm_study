#트리의 독립집합 2213
import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**9)
n=int(input())
cnt=[0]+list(map(int, input().split()))
visited= [False]*(n+1)
dp=[[0]*2 for i in range(n+1)]
tree=[[] for i in range(n+1)]

answer=[[[],[]] for _ in range(n+1)]

for i in range(n-1):
    a,b= map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(x):
    dp[x][0]=cnt[x]
    answer[x][0].append(x)
    for node in tree[x]:
        if not visited[node]:
            visited[node]=True
            dfs(node)
            if dp[node][0]>dp[node][1]:
                dp[x][1]+=dp[node][0]
                answer[x][1]+=answer[node][0]
            else:
                dp[x][1]+=dp[node][1]
                answer[x][1]+=answer[node][1]
            dp[x][0]+=dp[node][1]
            answer[x][0]+=answer[node][1]
visited[1]=True
dfs(1)


if dp[1][0]>dp[1][1]:
    print(dp[1][0])
    result=sorted(answer[1][0])
    print(*result)
else:
    print(dp[1][1])
    result=sorted(answer[1][1])
    print(*result)