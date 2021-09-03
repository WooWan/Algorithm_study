#10799 쇠막대기 스택 사용
import sys
input = sys.stdin.readline

stick = str(input())

pole = list()
result = 0
for i in range(len(stick)):
    if stick[i]=="(":
        pole.append(stick[i])
    elif stick[i]==")":
        if stick[i-1]=="(":
            pole.pop()
            result += len(pole)
        else:
            pole.pop()
            result +=1
print(result)

