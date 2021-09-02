# 1700 멀티탭 스케쥴링 G1
# os 의 lru와 비슷한 개념 g1보다 쉬운듯?

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

arr= list(map(int, input().split()))
scheduler = [deque() for i in range(k+1)]

for i in range(len(arr)):
    scheduler[arr[i]].append(i)
count = 0
tab =list()
result = 0
for i in range(k):
    if count<n:
        if not arr[i] in tab:
            tab.append(arr[i])
            count += 1
        scheduler[arr[i]].popleft()

    else:
        # 멀티탭에 이미 있는 경우
        if arr[i] in tab:
            scheduler[arr[i]].popleft()
        # 멀티탭에 없는 경우 가장 느리게 나오는 용품을 제거해야 한다
        else:
            target = tab[0]
            #tab 배열을 돈다
            for j in range(n):
                #다음에 사용안하는 경우 바로 제거하면 된다
                if not scheduler[tab[j]]:
                    target = tab[j]
                    break
                #다음에 사용하는 경우 가장 느리게 나오는 용품을 찾아야한다.
                else:
                    if scheduler[target][0]< scheduler[tab[j]][0]:
                        target = tab[j]
            scheduler[arr[i]].popleft()
            tab.remove(target)
            tab.append(arr[i])
            result+=1
print(result)

