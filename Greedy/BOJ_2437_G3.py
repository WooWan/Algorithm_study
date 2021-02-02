#누적합의 개념 묻는 문제
#sum_num+1보다 더 크다면 표현할수 없다
N = int(input())
nums = list(map(int, input().split()))
nums.sort()
sum_num = 0
for i in range(N):
	if sum_num + 1 >= nums[i]:
		sum_num += nums[i]
	else:
		break
print(sum_num + 1)
