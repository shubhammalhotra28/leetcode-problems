class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        /*
        Solution using two ptr appproach and 
        optimal solution that is changing the array instead of 
        creating space with another array and storing and then copying which is the other approach
        to solve it.
            */
        int j = 0; // ptr 1
        for(int i = 0;i<nums.size();i++) // loop
        {
            if(nums[i]!=0) // if i ptr is containing non zero
            {
                
                swap(nums[j],nums[i]); // swap with the other ptr
                j++; // inrement it
            }
        }
        
    }
};
