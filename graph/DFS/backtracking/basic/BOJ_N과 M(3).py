import sys
input = sys.stdin.readline

# 같은 문자를 선택을 허용하는 순열
# path dp 해당 문자열이 존재하는지 체크 안해주어도 된다
def solution():
    n, m = map(int, input().split())

    def dfs(path):
        if len(path) == m:
            print(' '.join(map(str, path)))
            return

        for number in range(1, n+1):
            dfs(path + [number])

    dfs([])

solution()