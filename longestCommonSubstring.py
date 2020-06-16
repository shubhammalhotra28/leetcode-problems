class Solution:
    # Recursive solution
    def lcs(self,str1,str2,i,j):
        
        if i==len(str1) or j==len(str2):
            return 0
        
        if str1[i] == str2[j]:
            ans = 1+self.lcs(str1,str2,i+1,j+1)
        else:
            ans1 = self.lcs(str1,str2,i+1,j)
            ans2 = self.lcs(str1,str2,i,j+1)
            ans = max(ans1,ans2)
        
        return ans
        
    
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        ans = self.lcs(text1,text2,0,0)
        return ans
        
       
####################################################################


class Solution:
    # Memoization
    def lcs(self,str1,str2,i,j,dp):
        
        if i==len(str1) or j==len(str2):
            return 0
        
        if str1[i] == str2[j]:
            if dp[i+1][j+1] == -1:
                smallAns = self.lcs(str1,str2,i+1,j+1,dp)
                dp[i+1][j+1] = smallAns
                ans = 1+smallAns
            else:
                ans = 1+dp[i+1][j+1]
        else:
            if dp[i+1][j] == -1:
                ans1 = self.lcs(str1,str2,i+1,j,dp)
                dp[i+1][j] = ans1
            else:
                ans1 = dp[i+1][j]
            if dp[i][j+1] == -1:
                ans2 = self.lcs(str1,str2,i,j+1,dp)
                dp[i][j+1] = ans2
            else:
                ans2 = dp[i][j+1]
            ans = max(ans1,ans2)
        
        return ans
        
    
    
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n = len(text1) #no of rows
        m = len(text2) #no of cols
        dp = [[-1 for j in range(m+1)]for i in range(n+1)]
        ans = self.lcs(text1,text2,0,0,dp)
        return ans
        
        
##################################################################


class Solution:
    # dp iterative soln
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n = len(text1)
        m = len(text2)
        
        dp = [[0 for j in range(m+1)]for i in range(n+1)]
        
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                
                if text1[i] == text2[j]:
                    dp[i][j] = 1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        
        
        return dp[0][0]
                
        
         
