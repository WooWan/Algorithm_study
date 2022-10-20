class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char)

        return strs == strs[::-1]


sol = Solution()
print(sol.isPalindrome("race a car"))
