#14938 서강 그라운드
import sys, heapq
input = sys.stdin.readline
INF= int(1e9)

n,m,r = map(int, input().split())

item = [0]+list(map(int, input().split()))
graph = [[] for i in range(n+1)]
for i in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((l,b))
    graph[b].append((l,a))


def dijkstra(start):
    distance = [INF] * (n + 1)
    distance[start]=0
    heap= list()
    heapq.heappush(heap,(0,start))
    while heap:
        cost, x = heapq.heappop(heap)

        if cost>distance[x]:
            continue
        for nextCost, nx in graph[x]:
            sum= cost+ nextCost
            if sum < distance[nx]:
                distance[nx]= sum
                heapq.heappush(heap, (sum, nx))
    return distance

answer = 0
for i in range(1,n+1):
    result= 0
    distance = dijkstra(i)
    for j in range(1, n+1):
        if distance[j]<=m:
            result += item[j]
    answer = max(answer, result)
print(answer)