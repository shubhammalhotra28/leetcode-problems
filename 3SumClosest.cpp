class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        
        sort(nums.begin(),nums.end());
        int min_diff = INT_MAX;
        int closest_ptr = 0;
        int n = nums.size();
        for(int i = 0;i<n-2;i++)
        {
            int low = i+1;
            int high = n-1;
            
            
            while(low<high)
            {
                int sum = nums[i]+nums[low]+nums[high];
            
                if(abs(target-sum) < abs(min_diff))
                {
                    min_diff = target-sum;
                    closest_ptr = sum;
                }
                if (sum > target)
                {
                    high--;
                }
                else if(sum < target)
                {
                   low++;
                }
                else
                {
                    return target;
                }
                    
            }
        }
        return closest_ptr;
        
        
        
    }
};










