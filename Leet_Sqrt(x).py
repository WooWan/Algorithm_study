# import math
#
#
# def mySqrt(x: int) -> int:
#     return math.trunc(math.sqrt(x))

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))


# 첫번째 생각 브루트 포스 => 3중 for문
# n = 10만 => O(nlogn)
# 2Aj = Ai+ Ak => 투 포인터?, 정렬이 되어 있지 않아서 될까..?
count = 0
for j in range(1,n-1):
    for i in range(j-1, -1, -1):
        for k in range(j+1, n):
            if 2*arr[j] == arr[i] + arr[k]:
                count+=1

print(count)