class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        
        
        if len(nums)==0:
            return 0
        
        left = 0
        ans = sys.maxsize
        
        sum = 0
        
        for i in range(len(nums)):
            
            sum += nums[i]
            
            while sum>=s:
                
                ans = min(ans,i-left+1)
                
                sum = sum-nums[left]
                left+=1
                
        return ans if ans is not sys.maxsize else 0
