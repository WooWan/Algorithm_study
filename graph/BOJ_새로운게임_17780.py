# import sys
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
#
# arr = [[[] for _ in range(n)] for _ in range(n)]
#
# for i in range(n):
#     arr[i].append(list(map(int, input().split())))
# # arr = [[[map(int, input().split())] for _ in range(n)] for _ in range(2)]
# print(arr)
# chess = []
# for i in range(k):
#     r, c, move = input().split()
#     direction = []
#     if move == 1:
#         direction = (0,1)
#     elif move == 2:
#         direction = (0,-1)
#     elif move == 3:
#         direction = (-1,0)
#     else:
#         direction = (1,0)
#     arr[r][c] = [i+1, direction]
#     print(arr)
#     chess.append((r,c, direction))
# print(arr)
# print(chess)
#
# # count = 0
# # while True:
# #     count += 1
# #     if count > 1000:
# #         print(-1)
# #         return
#

from sys import stdin
readline = stdin.readline

N, K = map(int, readline().split())
_map = [list(map(int, readline().split())) for _ in range(N)]
horses = [list(map(int, readline().split())) for _ in range(K)]
hmap = [[[] for _ in range(N)] for _ in range(N)]

dr, dc = (0, 0, -1, 1), (1, -1, 0, 0)

for i in range(len(horses)):
    hmap[horses[i][0]-1][horses[i][1]-1].append(i)

print(hmap)