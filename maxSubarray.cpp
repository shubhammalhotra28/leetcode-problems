class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        
        int maxSum = nums[0];
        int currSum = nums[0];
        int n = nums.size();
        for(int i=1;i<n;i++)
        {
            currSum = max(nums[i],nums[i]+currSum);
            maxSum = max(maxSum,currSum);
        }
        return maxSum;
        
    }
};
