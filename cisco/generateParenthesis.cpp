class Solution {
public:
    vector<string> generateParenthesis(int n) {
        
        vector<string> ans;
        backtracking(ans,"",0,0,n);
        return ans;
        
        
    }
    public :
    void backtracking(vector<string>& ans,string current,int open,int close,int max){
        
        if(current.length()==2*max)
        {
            ans.push_back(current);
            return;
        }
        
        if(open<max)
        {
            backtracking(ans,current+"(",open+1,close,max);
        }
        if(close<open)
        {
            backtracking(ans,current+")",open,close+1,max);
        }
        
    }
};
