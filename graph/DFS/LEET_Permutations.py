from typing import List

# 풀이 1.
# cur에 현재 노드를 담기
def permute(nums: List[int]) -> List[List[int]]:

    results = []
    def dfs(cur):
        if len(cur) == len(nums):
            results.append(cur[:])
            return

        for num in nums:
            if num not in cur:
                cur.append(num)
                dfs(cur)
                cur.pop()

    dfs([])

    return results

# 풀이2.
# 노드를 [1,2,3] 과 같은 집합으로 생각하기 [1] => [1,2] => [1,2,3]
def permute2(nums: List[int]) -> List[List[int]]:

    results = []
    current = []
    def dfs(elements):
        if len(elements) == 0:
            results.append(current[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            current.append(e)
            dfs(next_elements)
            current.pop()

    dfs(nums)
    return results



print(permute2([1,2,3]))