
import heapq
from typing import List

# def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
#     graph = [[] for _ in range(n+1)]
#     heap = []
#     for u,v,w in times:
#         graph[u].append([w,v])
#
#     distance = collections.defaultdict(int)
#
#     def dijkstra(start):
#         heapq.heappush(heap, [0, start])
#
#         while heap:
#             cost, node = heapq.heappop()
#             if node not in distance:
#
#     dijkstra(k)

import sys, heapq
import collections
INF=int(1e9)

n,m=map(int, sys.stdin.readline().split())
start= int(input())
graph=[[] for _ in range(n+1)]

dist = collections.defaultdict()
for i in range(m):
    u,v,w = map(int, sys.stdin.readline().split())
    graph[u].append((v,w))

def dijkstra(start):
    heap =[[0,start]]
    while heap:
        time, node = heapq.heappop(heap)
        if node not in dist:
            dist[node] = time
            for v,w in graph[node]:
                alt = time+w
                heapq.heappush(heap, (alt, v))

dijkstra(start)
for i in range(1,n+1):
    if i in dist:
        print(dist[i])
    else:
        print("INF")






