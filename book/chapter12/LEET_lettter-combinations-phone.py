from typing import List


def letterCombinations( digits: str) -> List[str]:

    def dfs(index, path):
        if len(path) == len(digits):
            result.append(path)
            return

        for i in range(index, len(digits)):
            print(dic[digits[i]])
            for j in dic[digits[i]]:
                # print(i,j)
                dfs(i+1, path+j)
    dic = {"2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6": "mno",
           "7": "pqrs", "8":"tuv", "9": "wxyz" }
    result =[]
    dfs(0,"")
    print(result)
    return result

letterCombinations("23")