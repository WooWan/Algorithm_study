import sys

sys.setrecursionlimit(10 ** 9)

##
def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for start, dest in edges:
        graph[start].append(dest)

    visited = [False] * len(info)
    answer = []
    answer2= []

    def dfs(x, sheep, wolf, canVisit):
        # visited[x] = True
        if info[x] == 1:
            wolf += 1
            if wolf >= sheep:
                return
        else:
            sheep += 1
            answer.append(sheep)

        canVisit.extend(graph[x])
        for animal in canVisit:
            dfs(animal, sheep, wolf, [i for i in canVisit if i != animal and i != x])

#  두 번째 풀이
    # edges를 돌며 parent가 방문, child를 방문하지 않았을 때만 dfs ,, 이런 아이디어는 어떻게 생각..,.??
    def dfs2(x, sheep, wolf):
        if info[x] == 1:
            wolf += 1
            if wolf >= sheep:
                return
        else:
            sheep += 1
            answer2.append(sheep)
        for i in range(len(edges)):
            parent, children = edges[i][0], edges[i][1]
            if visited[parent] and not visited[children]:
                visited[children] = True
                dfs2(children, sheep , wolf)
                visited[children] = False


    # dfs(0, 0, 0, [])
    visited[0] = True
    dfs2(0, 0,0)
    print(visited)
    return max(answer2)


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))

print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
               [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))
