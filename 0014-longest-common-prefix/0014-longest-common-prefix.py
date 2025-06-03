class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # first find the minimum length
        min_len = float("inf") 

        # make sure it doesnot go out of bound error
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)

        # now we comapare each letters
        i = 0
        while i < min_len:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i = i+1
        return s[:i]