class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        minimum = float('inf')

        for s in strs:
            if len(s) < minimum:
                minimum = len(s)

        i = 0
        while i < minimum:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1
        
        return s[:i]