class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        '''
        h - index :- refers to the index value where the the number at the ith index should be 
        greater than or equal to n - index
        '''
        
        
        n = len(citations)
        j=0
        for i in range(n):
            
            if citations[i]>=n-j:
                return n-j
            else:
                j+=1
        return 0
