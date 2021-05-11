#
import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

n=int(input())
menti= list(map(int, input().split()))
tree= [[] for i in range(n+1)]
visited=[False]*(n+1)
dp= [[0]*2 for _ in range(n+1)]
ability=[0]+list(map(int, input().split()))

for i in range(2,n+1):
    tree[menti[i-2]].append(i)

#0은 포함 1은 미포함
def dfs(x):
    #x가 포함되지 않을 때 모든 것을 다 더해주면 된다.
    for node in tree[x]:
        if not visited[node]:
            visited[node]=True
            dfs(node)
            dp[x][1]+=max(dp[node][0], dp[node][1])
    result=0
    #x가 포함될 경우는 child중에 하나가 멘토,멘티 관계여야한다.
    for node in tree[x]:

    for i in tree[x]:
        temp=0
        for j in tree[x]:
            #멘토,멘티 관계일 때 시너지를 곱해주고,
            if i==j: temp+=ability[x]*ability[i]
            else:
                #멘토, 멘티 관계가 아니라면 최대값을 더해준다.
                temp+=max(dp[j][0], dp[j][1])
        result=max(result, temp)
    dp[x][0]=result

visited[1]=True
dfs(1)
print(max(dp[1][0], dp[1][1]))