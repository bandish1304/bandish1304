class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # first initialize i and j to 0 and merge to " "
        i = 0
        j = 0
        merge = ""
        
        # Now do a while loop and make a merge
        while i < len(word1) and j < len(word2):
            merge += word1[i] + word2[j]
            i += 1
            j += 1
        # And then check is one word is greather than other
        if i < len(word1):
            merge += word1[i:]
        else:
            merge += word2[j:]
        return merge


        