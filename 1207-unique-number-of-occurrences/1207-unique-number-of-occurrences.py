# defaultdict set all numbers default to 0
from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = defaultdict(int)
        for nums in arr:
            counts[nums] += 1
        # Now we have to count the total(values) of each numbers
        occur = list(counts.values())
        # check if len(occur) is equal to set then return true
        # otherwise return false
        if len(occur) == len(set(occur)):
            return True
        else:
            return False