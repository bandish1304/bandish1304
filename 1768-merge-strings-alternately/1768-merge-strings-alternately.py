class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # first initialize i and j to 0 and merge to " "
        i = 0
        j = 0
        merge = ""
        len_w1 = len(word1)
        len_w2 = len(word2)
        
        # Now do a while loop and make a merge
        while i < len_w1 and j < len_w2:
            merge += word1[i] + word2[j]
            i += 1
            j += 1
        # And then check is one word is greather than other
        if i < len_w1:
            merge += word1[i:]
        else:
            merge += word2[j:]
        return merge


        