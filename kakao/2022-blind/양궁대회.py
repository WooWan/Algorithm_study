# import sys
# sys.setrecursionlimit(10**9)
#
# def solution(n, info):
#     # dfs로 풀 수 있을 것 같은데...
#     # 점수를 그래프의 노드로 생각하기 =>
#
#     winned = [False] * 11
#     def calDiff(lion):
#         lionScore = 0
#         peachScore = 0
#         for i in range(11):
#             if info[i] ==0 and lion[i] == 0: continue
#             if info[i] >= lion[i]:
#                 peachScore += 10 - i
#             else:
#                 lionScore += 10 - i
#         return lionScore - peachScore
#
#     def isBiggerArrow(x, lion):
#         if lion[x] > info[x]:
#             return True
#
#     result = []
#     lion = [0] * 11
#     def dfs(path, winned):
#         if sum(path) >= n:
#             # 라이언 점수
#             diff = calDiff(path)
#             if diff > 0:
#                 result.append([diff, path[:]])
#             return
#
#         for i in range(11):
#             if winned[i]:
#                 continue
#             path[10 - i] += 1
#             if isBiggerArrow(i, path):
#                 winned[i]= True
#             dfs(path, winned)
#             winned[i]= False
#             path[10-i] -= 1
#
#
#
#     dfs(lion, winned)
#     if len(result) == 0:
#         return [-1]
#     sortedScore = sorted(result, key = lambda x: x[0])
#     return sortedScore[-1][1]
#
#
#
# solution(5, [2,1,1,1,0,0,0,0,0,0,0])
# solution(1, 	[1,0,0,0,0,0,0,0,0,0,0])

import sys
sys.setrecursionlimit(10**9)

def solution(n, info):
    # dfs로 풀 수 있을 것 같은데...
    # 점수를 그래프의 노드로 생각하기 =>

    # winned = [False] * 11
    def calDiff(lion):
        lionScore = 0
        peachScore = 0
        for i in range(11):
            if info[i] == 0 and lion[i] == 0: continue
            if info[i] >= lion[i]:
                peachScore += 10 - i
            else:
                lionScore += 10 - i
        return lionScore - peachScore

    # def isBiggerArrow(x, lion):
    #     if lion[x] > info[x]:
    #         return True

    result = []
    lion = [0] * 11
    def dfs(path):
        if sum(path) >= n:
            # 라이언 점수
            diff = calDiff(path)
            if diff > 0:
                result.append([diff, path[:]])
            return

        for i in range(11):
            # if winned[i]:
            #     continue
            path[10 - i] += 1
            # if isBiggerArrow(i, path):
            #     winned[i]= True
            dfs(path)
            # winned[i]= False
            path[10-i] -= 1



    dfs(lion)
    if len(result) == 0:
        return [-1]
    sortedScore = sorted(result, key = lambda x: x[0])
    return sortedScore[-1][1]
