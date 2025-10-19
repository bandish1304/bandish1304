class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x = len(haystack)
        y = len(needle)

        if y == 0:
            return -1
        for i in range(x):
            if haystack[i:i+y] == needle:
                return i
        return -1
        