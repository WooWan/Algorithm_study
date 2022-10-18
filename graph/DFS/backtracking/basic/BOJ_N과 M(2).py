import sys
input = sys.stdin.readline

# 1부터 n까지 m개의 조합을 구하는 문제
# 순열과 달라진 점은, start를 추가해서 순서를 조정해주어야한다.
def solution():
    n, m = map(int, input().split())

    def dfs(path, start):
        if len(path) == m:
            print(' '.join(map(str, path)))
            return

        for number in range(start, n+1):
            if number in path:
                continue
            dfs(path + [number], number+1)

    dfs([], 1)

solution()