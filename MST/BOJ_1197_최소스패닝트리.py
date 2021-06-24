#1197 최소 스패닝트리

import sys
input=sys.stdin.readline

v,e= map(int, input().split())
parent=list(range(v+1))
edge=[]
for i in range(e):
    edge.append(list(map(int, input().split())))

#간선의 가중치에 따라 정렬해야한다.
edge.sort(key=lambda x: x[2])

answer=0
def union(a,b):
    a= findParent(a)
    b= findParent(b)
    if b < a:
        parent[a] = b
    else:
        parent[b] = a

def findParent(x):
    if x != parent[x]:
        parent[x]=findParent(parent[x])
    return parent[x]

#edge를 돌면서 서로 다른 집합일 경우 이어준다.
for a,b,value in edge:
    if findParent(a)!=findParent(b):
        union(a,b)
        answer+=value
print(answer)
