class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[1 for j in range(n)]for i in range(m)]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        
        return dp[m-1][n-1]
        
        
        
        
        
        '''
        if m==1 or n==1:
            return 1
        
        return self.uniquePaths(m,n-1)+self.uniquePaths(m-1,n)
        '''
        
        
        
