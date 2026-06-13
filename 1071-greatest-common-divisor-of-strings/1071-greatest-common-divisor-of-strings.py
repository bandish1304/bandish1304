class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # we need to find x
        # So first we need to check whether string1 and string 2 are equal
        if str1 + str2 != str2 + str1:
            return ""
        # Then we need to find greatest common divisor
        # Example ABCABC + ABC = ABCABCABC
        # The gcd of (6,3) is 3
        # So, it will take the first 3 characters of string1--> until size
        size = math.gcd(len(str1), len(str2))
        return str1[:size]
        