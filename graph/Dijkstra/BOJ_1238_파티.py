# 1238 파티
# 다익스트라 단방향 일 때, 반대방향은 간선을 뒤집는 것과 동일하다
import sys, heapq

n,m,x= map(int, sys.stdin.readline().split())
INF=1e9
graph=[[] for _ in range(n+1)]
reverse=[[] for _ in range(n+1)]
visited = [False]*(n+1)
for i in range(m):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((w, v))
    reverse[v].append((w,u))


def dijkstra(start, town):
    heap = list()
    heapq.heappush(heap, (0, start))
    distance = [INF]*(n+1)
    distance[start]=0

    while heap:
        cost, x= heapq.heappop(heap)
        if distance[x] < cost:
            continue
        for nextCost, nx in town[x]:
            sum=cost+nextCost
            if sum<distance[nx]:
                distance[nx]=sum
                heapq.heappush(heap, (distance[nx], nx))
    return distance


result=dijkstra(x, graph)
reverseResult= dijkstra(x, reverse)
# x로부터 각 노드로 가는 시간
answer=0
# i로부터 x번 마을로 가는 시간
for i in range(1,n+1):
    answer=max(answer, result[i] + reverseResult[i])

print(answer)