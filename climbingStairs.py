class Solution:
    
    def climbStairsHelper(self,n,dp):
        
        if n<0:
            return 0
        if n==0:
            return 1
        
        if dp[n-1]==-1:
            ans1 = self.climbStairsHelper(n-1,dp)
            dp[n-1] = ans1
        else:
            ans1 = dp[n-1]
        if dp[n-2]==-1:
            ans2 = self.climbStairsHelper(n-2,dp)
            dp[n-2] = ans2
        else:
            ans2 = dp[n-2]
        return ans1+ans2
    
    
    def climbStairs(self, n: int) -> int:
        
        # memoization
        dp = [-1 for i in range(n+1)]
        return self.climbStairsHelper(n,dp)
        
        '''
        if n<0:
            return 0
        if n==0:
            return 1
        return self.climbStairs(n-1)+self.climbStairs(n-2)
        '''
