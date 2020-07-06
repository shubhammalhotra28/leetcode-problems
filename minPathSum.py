class Solution:
    
    def minPathSumHelper(self,grid):
        n = len(grid)
        m = len(grid[0])
        dp = [[sys.maxsize for j in range(m+1)]for i in range(n+1)]
        
        for i in range(n-1,-1,-1):
            
            for j in range(m-1,-1,-1):
                
                if i == n-1 and j==m-1:
                    
                    dp[i][j] = grid[i][j]
                else:
                    dp[i][j] = grid[i][j]+min(dp[i+1][j],dp[i][j+1])
        
        return dp[0][0]
        
    
    
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        return self.minPathSumHelper(grid)
        # iteratively dp
