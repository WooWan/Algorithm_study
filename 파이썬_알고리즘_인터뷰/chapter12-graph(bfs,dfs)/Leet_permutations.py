from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        check = [False] * len(nums)

        # check을 통해 사용한 값을 체크
        def dfs(index, path):
            if index == len(nums):
                answer.append(path)

            for i in range(len(nums)):
                if check[i]:
                    continue
                check[i] = True
                dfs(index + 1, path + [nums[i]])
                check[i] = False

        # 2번째 풀이 사용한 value를 array 상에서 삭제시켜준다
        # def dfs(index, path, rest):
        #     if index == len(nums):
        #         answer.append(path)
        #         return
        #     for value in rest:
        #         copyArr = rest[:]
        #         copyArr.remove(value)
        #         dfs(index+1, path +[value], copyArr)


        dfs(0, [], nums)
        print(answer)
sol = Solution()
sol.permute([0,1])