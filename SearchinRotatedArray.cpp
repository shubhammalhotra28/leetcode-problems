class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size()-1;
        
        while(left<=right)
        {
            int mid = (left+right)/2;
            int midValue = nums[mid];
            int currLeft = nums[left];
            int currRight = nums[right];
            if(midValue==target)
            {
                return mid;
            }
            if(midValue<currLeft)
            {
                if(target > midValue && target <= currRight)
            {
                left = mid+1;
                
            }
            else
            {
                right = mid-1;
            }
            }
            else if (midValue > currRight)
            {
                if(target < midValue && target>=currLeft)
                {
                    right = mid-1;
                }
                else
                {
                    left = mid+1;
                }
            }
            else
            {
                if(target>midValue)
                {
                    left = mid+1;
                }
                else
                {
                    right = mid-1;
                }
            }
        }
        return -1;
    }
};













