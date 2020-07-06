class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        maxProfit = 0
        minprice = sys.maxsize
        
        for i in range(len(prices)):
            
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i]-minprice > maxProfit:
                maxProfit = prices[i]-minprice
        
        
        return maxProfit
            
        #BRUTE FORCE  
        '''
        maxProfit = 0
        
        for i in range(0,len(prices)):
            
            for j in range(i+1,len(prices)):
                
                profit = prices[j]-prices[i]
                
                if profit>maxProfit:
                    maxProfit = profit
                    
        return maxProfit
        '''
