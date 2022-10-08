from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        check = [False] * len(nums)

        def dfs(index, path):
            if index == len(nums):
                answer.append(path)

            for i in range(len(nums)):
                if check[i]:
                    continue
                check[i] = True
                temp = nums[i]
                dfs(index + 1, path + [temp])
                check[i] = False

        dfs(0, [])
        print(answer)
sol = Solution()
sol.permute([0,1])