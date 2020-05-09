class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<string,int> map;
        vector<vector<string>> res;
        for(auto str : strs)
        {
            string newstr = str;
            sort(newstr.begin(),newstr.end());
            if(map.count(newstr)>=1)
            {
                res[map[newstr]].push_back(str);
            }
            else
            {
                map.insert({newstr,res.size()});
                res.push_back({str});
                
            }
        }
        return res;
    }
};




