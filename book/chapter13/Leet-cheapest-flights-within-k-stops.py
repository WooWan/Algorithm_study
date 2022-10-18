import collections
import heapq
import sys
from typing import List

INF = 1e9

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    graph = collections.defaultdict(list)
    weight = [sys.maxsize] * n
    # 그래프 인접 리스트 구성
    for u, v, w in flights:
        graph[u].append((v, w))

    # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
    Q = [(0, src, K)]

    # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                if alt < weight[v]:
                    weight[v] = alt
                    heapq.heappush(Q, (alt, v, k - 1))
    # print(weight)
    return -1

    # def dijkstra(start):
    #     heap = [[0, start, 0]]
    #     while heap:
    #         acc, node, layover = heapq.heappop(heap)
    #         if node == dst:
    #             return acc
    #         if layover > k:
    #             continue
    #         for cost, nextNode in graph[node]:
    #             # 그리디하게 탐색하지 않아도 된다
    #             sum = acc + cost
    #             heapq.heappush(heap, (sum, nextNode, layover + 1))
    #     return -1

    # graph = [[] for _ in range(n)]
    # for flight in flights:
    #     u, v, w = flight
    #     graph[u].append((w, v))
    #
    # heap = [[0, src, 0]]
    #
    # while heap:
    #     acc, node, layover = heapq.heappop(heap)
    #     if node == dst:
    #         return acc
    #     if layover <= k:
    #         layover +=1
    #         for cost, nextNode in graph[node]:
    #             # 그리디하게 탐색하지 않아도 된다
    #             sum = acc + cost
    #             heapq.heappush(heap, (sum, nextNode, layover ))
    # return -1



print(findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3,1))
print(findCheapestPrice(13,
[[11,12,74],[1,8,91],[4,6,13],[7,6,39],[5,12,8],[0,12,54],[8,4,32],[0,11,4],[4,0,91],[11,7,64],[6,3,88],[8,5,80],[11,10,91],[10,0,60],[8,7,92],[12,6,78],[6,2,8],[4,3,54],[3,11,76],[3,12,23],[11,6,79],[6,12,36],[2,11,100],[2,5,49],[7,0,17],[5,8,95],[3,9,98],[8,10,61],[2,12,38],[5,7,58],[9,4,37],[8,6,79],[9,0,1],[2,3,12],[7,10,7],[12,10,52],[7,2,68],[12,2,100],[6,9,53],[7,4,90],[0,5,43],[11,2,52],[11,8,50],[12,4,38],[7,9,94],[2,7,38],[3,7,88],[9,12,20],[12,0,26],[10,5,38],[12,8,50],[0,2,77],[11,0,13],[9,10,76],[2,6,67],[5,6,34],[9,7,62],[5,3,67]]
,10
,1
,10))
# print(findCheapestPrice(5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0, 2,2))
# print(distance)