class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l, r = 0, 0

        for i in range(len(s)):
            if s[i] == "(":
                r += 1
            elif r > 0:
                r -= 1
            else:
                l += 1

        return l + r
