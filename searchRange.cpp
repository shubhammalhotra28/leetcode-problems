class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        
        vector<int> res;
        int size = nums.size();
        int l = 0;
        int r = size-1;
        int left = -1;
        int right = -1;
        int flag = -1;
        
        if(size==0)
            return {-1,-1};
        
        while(l<=r)
        {
            int mid = (l+r)/2;
            if(nums[mid]>target)
            {
                r = mid-1;
            }
            else if(nums[mid]<target)
            {
                l = mid+1;
            }
            else
            {
                flag = mid;
                break;
            }
        }
        
        if(flag==-1)
        {
            return {-1,-1};
        }
        else
        {
            left = flag;
            right = flag;
            while(1)
            {
                int temp = left-1;
                if(temp>=0 && nums[temp]==target)
                {
                    left = temp;
                }
                else{
                    break;
                }
            }
            
             while(1)
            {
                int temp = right+1;
                if(temp<size && nums[temp]==target)
                {
                    right = temp;
                }
                else{
                    break;
                }
            }
            
            res.push_back(left);
            res.push_back(right);
            
        }
        
        return res;
        
    }
};
