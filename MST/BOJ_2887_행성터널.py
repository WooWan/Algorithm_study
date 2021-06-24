#2887 행성터널
#각 좌표를 입력받을때 i를 부여한다.
#모든 거리를 구할시에 v^^2이지만 문제의 조건에 따라 특정거리만 구하면 된다 good
import sys
input= sys.stdin.readline

n=int(input())
coord=[]
#각 좌표 i를 미리 지정해주는 방식** 유용
for i in range(n):
    x,y,z= map(int, input().split())
    coord.append((x,y,z,i))
parent= [i for i in range(n)]
edge=[]

def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]
def union(a,b):
    a=find(a)
    b=find(b)
    parent[max(a,b)]=min(a,b)

for i in range(3):
    coord.sort(key=lambda x: x[i])
    for j in range(1,n):
        edge.append((coord[j][3],coord[j-1][3], abs(coord[j][i]-coord[j-1][i])))

edge.sort(key= lambda x: x[2])
answer=0
for x,y,value in edge:
    if find(x)!=find(y):
        answer+=value
        union(x,y)

print(answer)
