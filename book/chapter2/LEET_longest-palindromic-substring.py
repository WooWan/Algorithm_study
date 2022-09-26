class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(word):
            if word == word[::-1]: return True
            return False

        answer = ""

        for index, value in enumerate(s):
            for j in range(index + 1, len(s)):
                temp = s[index:j + 1]
                if len(answer) > len(temp): continue
                if isPalindrome(temp):
                    answer = temp
        print(answer)
        return answer

sol = Solution()
sol.longestPalindrome("a")