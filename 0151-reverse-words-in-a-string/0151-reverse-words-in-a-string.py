class Solution:
    def reverseWords(self, s: str) -> str:
    # so first we have to take extra space from the beginning and end
        s = s.strip()
    # Then we have to seperate the words
        words = s.split()
    # Then we have to reversed the words
        reverse_words = words[::-1]
    # and then we have to join the words as a string
        return' '.join(reverse_words)
    
        