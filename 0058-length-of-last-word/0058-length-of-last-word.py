class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        count = 0

        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            i -= 1
            count += 1

        return count
        