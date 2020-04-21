class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int target) {
        sort(nums.begin(),nums.end());
        int n = nums.size();
        int count = 0;
        
        for(int i = 0;i<n-2;i++)
        {
            int low = i+1;
            int high = n-1;
            
            while(low<high)
            {
                int sum = (nums[i]+nums[low]+nums[high]);
                if(sum<target)
                {
                    count += high-low; // tells us how many index pairs contains low {(low,i),(low,i+1)......(low,high)}
                    low++;
                }
                else
                {
                    high--;
                }
            }
        }
        return count;
    }
};
