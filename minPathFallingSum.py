class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        n = len(A)
        m = len(A[0])
        ans = sys.maxsize
  

        def helper(i,j,dp):

            if j>m-1 or j<0 :
      
                return sys.maxsize
    
            if i==n-1:
                return A[i][j]
    
            if dp[i+1][j-1]==-1:
                ans1 = helper(i+1,j-1,dp)
                dp[i+1][j-1] = ans1
            else:
                ans1 = dp[i+1][j-1]
            if dp[i+1][j]==-1:
                ans2 = helper(i+1,j,dp)
                dp[i+1][j]=ans2
            else:
                ans2 = dp[i+1][j]
            if dp[i+1][j+1]==-1:
                ans3 = helper(i+1,j+1,dp)
                dp[i+1][j+1] = ans3
            else:
                ans3 = dp[i+1][j+1]

            return A[i][j]+min(ans1,ans2,ans3)

        
        dp = [[-1 for j in range(m+1)] for i in range(n+1)]
        for j in range(m):

            ans = min(ans,helper(0,j,dp))
        
        return ans 
