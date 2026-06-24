class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s) #convert the strings into list
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        # This can be solved by two pointers
        # we define left and right
        l = 0
        r = len(s)-1

        while l < r:
            if s[l] not in vowels:
                l += 1
            elif s[r] not in vowels:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)


        