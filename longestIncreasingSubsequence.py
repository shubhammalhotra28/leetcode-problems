# dp iteratively

class Solution:
    
    def lis(self,nums,n):
        
        dp = [[0 for i in range(2)] for j in range(n+1)]
        
        for i in range(n-1,-1,-1):
            
            including_max = 1
            
            for j in range(i+1,n):
                
                if nums[j]>nums[i]:
                    
                    including_max = max(including_max,1+dp[j][0])
            
            dp[i][0] = including_max
            
            excluding_max = dp[i+1][1]
            
            overallMax = max(including_max,excluding_max)
            
            dp[i][1] = overallMax
            
        
        return dp[0][1]
            
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans = self.lis(nums,n)
        return ans
        
        

# memoization 
class Solution:
    
    def lis(self,nums,i,n,dp):
        
        if i==n:
            return 0,0
        
        including_max = 1
        for j in range(i+1,n):
            
            
            if nums[j]>nums[i]:
                if dp[j]==-1:
                    ans = self.lis(nums,j,n,dp)
                    dp[j] = ans
                    
                    further_including_max = ans[0]
                else:
                    
                    further_including_max = dp[j][0]
                    
                including_max = max(including_max,1+further_including_max)
        
        if dp[i+1]==-1:
            ans = self.lis(nums,i+1,n,dp)
            dp[i+1] = ans
            excluding_max = ans[1]
        
        else:
            excluding_max = dp[i+1][1]
        overallMax = max(including_max,excluding_max)
        
        return including_max,overallMax
        
        
        
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for i in range(n+1)]
        ans,ans1 = self.lis(nums,0,n,dp)
        
        return ans1
        
        
        


# recursion 
class Solution:
    
    def lis(self,nums,i,n):
        
        if i==n:
            return 0,0
        
        including_max = 1
        for j in range(i+1,n):
            
            if nums[j]>nums[i]:
                
                further_including_max = self.lis(nums,j,n)[0]
                including_max = max(including_max,1+further_including_max)
        
        excluding_max = self.lis(nums,i+1,n)[1]
        
        overallMax = max(including_max,excluding_max)
        
        return including_max,overallMax
        
        
        
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans,ans1 = self.lis(nums,0,n)
        
        return ans1
        
        
        
