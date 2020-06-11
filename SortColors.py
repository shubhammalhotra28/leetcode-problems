class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        next_one = 0
        next_two = len(nums)-1
        
        while i<=next_two:
            
            if nums[i]==0:
                nums[i],nums[next_one] = nums[next_one],nums[i]
                i+=1
                next_one+=1
            elif nums[i]==1:
                i+=1
            else:
                # if 2
                nums[i],nums[next_two] = nums[next_two],nums[i]
                next_two-=1
            
            
