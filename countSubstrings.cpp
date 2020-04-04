class Solution {
public:
    int countSubstrings(string s) {
        
        int n = s.length();
        int substrings = 0;
        
        for(int i = 0;i<2*n-1;i++)
        {
            int left = i/2;
            int right = left+i%2;
            while(left>=0 && right<n && s[left] == s[right])
            {
                left--;
                right++;
                substrings++;
            }
        }
        
        return substrings;
        
        
    }
};
