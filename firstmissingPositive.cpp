class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
    
        int n = nums.size();
        if(n==0)
            return 1;
        
        int arr[n+1] = {0};
    
        
         for(auto x : nums)
         {
             if(x>0 && x<=n)
             {
                 arr[x-1] = x;
             }
         }
        
        for(int i = 0;i<=n;i++)
        {
            if(arr[i]!=i+1)
            {
                return i+1;
            }
        }
        return n;
    
        
        
    }
};
