from typing import List

def letterCombinations(digits: str) -> List[str]:

    cases = {
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    results = []
    def dfs(index, cur):
        if len(cur) == len(digits):
            results.append(cur)
            return

        for item in cases[digits[index]]:
            dfs(index+1, cur + item)

    dfs(0, "")
    return results

inp = "23"