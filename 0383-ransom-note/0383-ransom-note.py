class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # First open the counter
        counter = {}
        #then do for the magazine
        for x in magazine:
            if x in counter:
                counter[x] += 1
            else:
                counter[x] = 1
        # And then do for the ransomNote
        for x in ransomNote:
            if x not in counter:
                return False
            elif counter[x] == 1:
                del counter[x]
            else:
                counter[x] -= 1
        return True

        
        