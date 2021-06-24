#1774 우주신과의 교감
#MST
import math
import sys
input=sys.stdin.readline

N,M=map(int, input().split())
parent= [i for i in range(N+1)]

def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a= find(a)
    b= find(b)
    parent[math(a,b)]=min(a,b)
coord=[]
edge=[]
for i in range(N):
    x,y= map(int, input().split())
    coord.append((x,y))

#이미 연결된 두 점
for i in range(M):
    a,b= map(int, input().split())
    union(a-1,b-1)

def dist(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

for i in range(N-1):
    for j in range(i+1,N):
        edge.append((i,j, dist(coord[i],coord[j])))
edge.sort(key=lambda x: x[2])

answer=0

for a,b,value in edge:
    if find(a)!=find(b):
        answer+=value
        union(a,b)
print('%.2f' %(answer))