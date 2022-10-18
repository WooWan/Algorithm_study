import sys
input = sys.stdin.readline

# 1부터 n까지 m개의 순열을 구하는 문제
def solution():
    n, m = map(int, input().split())

    def dfs(path):
        if len(path) == m:
            print(' '.join(map(str, path)))
            return

        for number in range(1, n+1):
            if number in path:
                continue
            dfs(path + [number])

    dfs([])


solution()