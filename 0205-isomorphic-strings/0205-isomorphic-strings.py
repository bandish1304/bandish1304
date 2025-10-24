class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # first we create two map of strings
        mapST = {}
        mapTS = {}

        # Then we create the characters for maps
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]

        # we check if else conditions
            if ((c1 in mapST and mapST[c1] != c2) or
                (c2 in mapTS and mapTS[c2] != c1)):
                return False

        # Then we connect characters of the mappings
            mapST[c1] = c2
            mapTS[c2] = c1

        return True