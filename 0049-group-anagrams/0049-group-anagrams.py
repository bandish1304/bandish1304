class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # This creates a key with empty list

        # Now iterate through input strings and 
        # make all of them 0
        for s in strs:
            count = [0] * 26

        # Now find each letter index values
            for c in s:
                count[ord(c) - ord('a')] += 1

        # and then append
            res[tuple(count)].append(s)
        return list(res.values())