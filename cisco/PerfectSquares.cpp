class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n+1,0);
        
        dp[0] = 0;
        dp[1] = 1;
        
        for(int i = 2;i<=n;i++)
        {
            dp[i] = INT_MAX;
            int j = 1;
            while((j*j)<=i)
            {
                dp[i] = min(dp[i],dp[i-(j*j)]+1);
                j++;
            }
        }
        return dp[n];
    }
};
