class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # Now create a Hashmap
        countS = {}
        countT = {}

        # Then put all the characters in hashMap
        # Build the hashmap
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Next we want to iterate the hashmaps
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
        