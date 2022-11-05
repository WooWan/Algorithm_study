import collections
from collections import deque
from typing import List


def findItinerary(tickets: List[List[str]]) -> List[str]:
    airlines = collections.defaultdict(deque)
    route = []

    def dfs(curNode):
        while airlines[curNode]:
            dfs(airlines[curNode].popleft())
        route.append(curNode)

    for airline in tickets:
        start, end = airline
        airlines[start].append(end)

    for node in airlines:
        airlines[node] = deque(sorted(airlines[node]))
    dfs("JFK")

    return route[::-1]
#
# findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT", "JFK"]])
findItinerary([["JFK","KUL"],["JFK","NRT"], ["NRT", "JFK"]])
