class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums)==0:
            return [[]]
        
        smallerOutput = self.subsets(nums[1:])
        
        outputLen = len(smallerOutput)
        
        for i in range(outputLen):
            smallerOutput.append(smallerOutput[i].copy())
            smallerOutput[i+outputLen].append(nums[0])
        
        return smallerOutput
