# import sys
# from collections import deque
#
# t=int(input())
#
# def bfs(x):
#     queue=deque()
#     visited[x]=True
#     queue.append(x)
#
#     while queue:
#         x=queue.popleft()
#         #방문한적이 있다면,
#         nx=arr[x]
#         if visited[nx]:
#             if not finished[nx]:
#                 # print(f' nx:{nx} x:{x}')
#                 team[nx]=True
#                 start=nx
#                 nx=arr[nx]
#                 while start!=nx:
#                     if nx == arr[nx]:
#                         team[nx] = True
#                         return
#                     # nx=arr[nx]
#                     team[nx]=True
#                     nx=arr[nx]
#         else:
#             visited[nx]=True
#             queue.append(nx)
# for _ in range(t):
#     n=int(sys.stdin.readline())
#     visited=[False]*(n+1)
#     team=[False]*(n+1)
#     finished=[False]*(n+1)
#     arr=[0]+list(map(int, sys.stdin.readline().split()))
#     for i in range(1,n+1):
#         if i==arr[i]:
#             team[i]=True
#             continue
#         if not visited[i]:
#             # visited=[False]*(n+1)
#             bfs(i)
#     print(team)
#     print(n-team.count(True))

#bfs를 통해서 구현해보려고 했으나 실패
#
# import sys
# sys.setrecursionlimit(100000)
# t= int(input())
#
# def dfs(x):
#     global cnt
#     visited[x]=True
#     nx=arr[x]
#     if not visited[nx]: dfs(nx)
#     else:
#         if not finished[nx]:
#             current= nx
#             while current!=x:
#                 cnt+=1
#                 current=arr[current]
#             cnt+=1
#     finished[x]=True
#
#
# for _ in range(t):
#     n=int(input())
#     arr=[0]+list(map(int, sys.stdin.readline().split()))
#     visited= [False]*(n+1)
#     finished=[False]*(n+1)
#     cnt=0
#
#     for i in range(1,n+1):
#         if not visited[i]:
#             dfs(i)
#     print(n-cnt)

import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**7)

t=int(input())
def dfs(x):
    global result
    visited[x]=True
    nx=array[x]
    if not visited[nx]:
        dfs(nx)
    else:
       if not finished[nx]:
           current= nx
           result+=1
           while current!=x:
               result+=1
               current=array[current]
    finished[x]=True


for _ in range(t):
    n=int(input())
    visited=[False]*(n+1)
    finished=[False]*(n+1)
    result=0
    array=[0]+list(map(int, input().split()))
    for i in range(1,n+1):
        if not visited[i]:
            dfs(i)
    print(n-result)
