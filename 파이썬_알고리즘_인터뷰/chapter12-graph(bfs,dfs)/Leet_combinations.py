from typing import List


def combine(n: int, k: int) -> List[List[int]]:
    answer =[]

    def dfs(elements, start):
        if len(elements) == k:
            answer.append(elements[:])
            return

        for i in range(start, n+1):
            elements.append(i)
            # start + 1 이 아닌, i + 1로 넘겨야 한다.
            # ex: 1,3 => i = 3
            dfs(elements, i+1)
            elements.pop()


    dfs([], 1)
    return answer
combine(5,3)