class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height)==0:
            return 0
        
        size = len(height)
        leftMax = [None for i in range(size)]
        rightMax = [None for i in range(size)]
        totalWater = 0
        
        leftMax[0] = height[0]
        
        for i in range(1,size):
            
            leftMax[i] = max(height[i],leftMax[i-1])
        
        rightMax[size-1] = height[size-1]
        
        for i in range(size-2,-1,-1):
            
            rightMax[i] = max(height[i],rightMax[i+1])
        
        for i in range(1,size):
            
            totalWater += min(leftMax[i],rightMax[i]) - height[i]
        
        return totalWater
