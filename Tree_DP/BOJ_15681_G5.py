
#15681 트리와 쿼리
#기본적인 트리 DP문제
#트리 dp의 기본적인 아이디어는 tree[n]= tree[1]+tree[2]+...+tree[n](n=연결된 노드의 개수)
import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**9)

n,r,q= map(int,input().split())
tree=[[] for i in range(n+1)]
visited=[False]*(n+1)
dp=[1]*(n+1)

def dfs(x):
    for num in tree[x]:
        if not visited[num]:
            visited[num] = True
            dp[x]+=dfs(num)
    return dp[x]

for i in range(n-1):
    u,v=map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
visited[r]=True
dfs(r)
for i in range(q):
    n= int(input())
    print(dp[n])