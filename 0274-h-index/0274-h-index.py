class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Make a count array
        count = [0] * (len(citations) + 1)
        # Then do a for loop
        for item in citations:
            if item > len(citations):
                count[len(citations)] += 1
            else:
                count[item] += 1
        # Now go backward loop
        total_citations = 0
        for i in range(len(count)-1, -1, -1):
            total_citations += count[i]
            if total_citations >= i:
                return i
        return 0
        