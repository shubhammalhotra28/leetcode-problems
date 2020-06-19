class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()
        n = len(citations)
        idx = 0
        for i in range(n):
            
            if citations[i]>=n-idx:
                return n-idx
            else:
                idx+=1
        return 0
