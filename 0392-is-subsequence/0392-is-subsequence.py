class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
    #First we create two pointers i and j
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
    # Now check if i is at the last character then its true or its false
        if i == len(s):
            return True
        else:
            return False
