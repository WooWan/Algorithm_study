#1976 여행 가자
#Union find 기본
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
parent=[i for i in range(n+1)]

#find x!=parent[x] -> root 노드가 아니라면, parent를 탐색한다
def findParent(x):
    if x!=parent[x]:
        parent[x]=findParent(parent[x])
    return parent[x]
#둘의 root까지 탐색한 뒤, 작은 것이 root로 설정한다
def union(a,b):
    a=findParent(a)
    b=findParent(b)
    if a>b:
        parent[a]=b
    else: parent[b]=a


for i in range(m):
    e,a,b= map(int,input().split())
    if e==0:
        union(a,b)
    else:
        a=findParent(a)
        b=findParent(b)
        if a==b:
            print("YES")
        else: print("NO")
