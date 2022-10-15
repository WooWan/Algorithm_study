from typing import List


def letterCombinations(digits: str) -> List[str]:
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
           "7": "pqrs", "8": "tuv", "9": "wxyz"}
    result = []

    def dfs(index, curStr):
        if len(curStr) == len(digits):
            result.append(curStr)
            return

        for c in dic[digits[index]]:
            dfs(index + 1, curStr + c)

    if digits:
        dfs(0, "")
    return result

letterCombinations("23")