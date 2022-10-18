import sys
input = sys.stdin.readline

# 1부터 n까지 m개의 조합을 구하는 문제
# 같은 수의 중복을 허용하는 조합
def solution():
    n, m = map(int, input().split())

    def dfs(path, start):
        if len(path) == m:
            print(' '.join(map(str, path)))
            return

        for number in range(start, n+1):
            dfs(path + [number], number)

    dfs([], 1)

solution()