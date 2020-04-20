// one iteration using hashmap

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> v;
        for(int i = 0;i<nums.size();i++)
        {
            int diff = target-nums[i];
            if(v.count(diff)) // finds if v.count(diff) is true
            {
                vector<int> ans;
                ans.push_back(v[diff]);
                ans.push_back(i);
                return ans;
            }
            v[nums[i]] = i;
        }
       return {}; 
    }
};




// Brute force approach
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        vector<int> v;
        for(int i =0;i<nums.size();i++){
            for(int j = i+1;j<nums.size();j++)
            {
                if(target == nums[i]+nums[j]){
                    v.push_back(i);
                    v.push_back(j);
                }
            }
        }
        return v;
        
    }
};
