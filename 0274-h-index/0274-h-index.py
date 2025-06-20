class Solution:
    def hIndex(self, citations: List[int]) -> int:
        counts = [0] *(len(citations) + 1)

        for item in citations:
            if item >= len(citations):
                counts[len(citations)] += 1
            else: 
                counts[item] += 1

        total_citations = 0
        for i in range(len(counts) -1, -1, -1):
            total_citations += counts[i]
            if total_citations >= i:
                return i
        return 0
