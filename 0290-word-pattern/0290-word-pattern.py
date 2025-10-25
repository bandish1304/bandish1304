class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False
        
        chartoWord = {}
        wordtoChar = {}

        for c, w in zip(pattern, words):
            if c in chartoWord and chartoWord[c] != w:
                return False
            if w in wordtoChar and wordtoChar[w] != c:
                return False

            chartoWord[c] = w
            wordtoChar[w] = c
        return True