class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max_len = 0
        d = {}

        while end < len(s):
        #first check if there is no repeating characters in dictionary
            if s[end] in d and d[s[end]] >= start:
                start = d[s[end]] + 1
        # Then update max length
            max_len = max(max_len, end - start + 1)
            d[s[end]] = end
            end += 1
        return max_len