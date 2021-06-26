#2252 줄 세우기
#위상정렬 기본 개념
#위상정렬: 자신보다 선행되어야 할 일이 있을 때(선행조건) 위상정렬이 필요하다
#따라서 유향 그래프여야 하고(방향 O), 사이클이 존재하면 안된다.
#여러가지 답이 존재할 수 있다

#선행조건은 indegree로 표현되며, indegree=0인 node들을 queue에 넣고, queue의 정점들을 돌면서 그 정점에서 나가는 간선들을 삭제한다
#(indegree-=1), indegree가 0이라면 선행조건을 모두 만족시켰으므로 queue에 삽입하고 이를 queue가 빌 때까지 반복한다.
import sys
from collections import deque

input=sys.stdin.readline
queue=deque()

n,m= map(int, input().split())
graph=[[] for i in range(n+1)]
indegree=[0]*(n+1)

for i in range(m):
    #a가 b 앞에 서야함
    a,b= map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1

for i in range(1, n+1):
    if indegree[i]==0:
        queue.append(i)

while queue:
    x= queue.popleft()
    for j in graph[x]:
        indegree[j]-=1
        if indegree[j]==0:
            queue.append(j)
    print(x, end=' ')






