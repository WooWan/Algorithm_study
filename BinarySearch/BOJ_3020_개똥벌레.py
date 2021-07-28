## 개똥벌레 gold 5 이분탐색 result 대신 start,end return하기.
import sys
input= sys.stdin.readline

n,h= map(int, input().split())
bottom = list()
top = list()

for i in range(n):
    if i % 2 == 0:
        bottom.append(int(input()))
    else:
        top.append(int(input()))

top.sort()
bottom.sort()
minCount=n
count=0
def binarySearch(array, target):
    start, end= 0, len(array)-1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    #전체 개수에서 (end+1)을 빼주면 target보다 큰 데이터의 개수이다.(index=0부터 시작하기 때문!!)
    return len(array)-end+1

for i in range(1,h+1):
    temp= binarySearch(bottom, i) + binarySearch(top, h - i + 0.5)
    if minCount> temp:
        count=1
        minCount=temp
    elif minCount==temp:
        count+=1

print(minCount, count)




