class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ["flower", "flow", "flight"]
        # So first we have to define the prefix
        # that is the first word in strings which is strs[0]
        prefix = strs[0]
        for i in range(len(prefix)):
            for word in strs:    # This will check every word in strings
                if i == len(word) or prefix[i] != word[i]:
                    return prefix[:i]  # This will give the words till match
        return prefix