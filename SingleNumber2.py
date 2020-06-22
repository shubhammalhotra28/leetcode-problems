# using o(n) space
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else:
                dict[nums[i]] = 1
        ans = -1000
        for i in range(len(nums)):
            if dict[nums[i]]==1:
                ans = nums[i]
        return ans


#using O(1) space :
# using bitwise operators
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        
        seen_once = 0
        seen_twice = 0
        
        for num in nums:
            
            seen_once = ~seen_twice&(seen_once^num)
            seen_twice = ~seen_once&(seen_twice^num)
            
        return seen_once
            
