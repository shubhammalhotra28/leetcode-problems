int decodeWays(string s){

	if(s == "0" || s[0] == '0')
	{
		return 0;
	}

	int n = s.size();
	s[0] = 1;
	s[1] = 1;
	vector<int> dp(n+1,0);
	for(int i = 2;i<n;i++)
	{
		if(s[i-1]!='0')
		{
			dp[i] += dp[i-1]; 
		}
		if(dp[i-1] < '7' && dp[i-2] == '2' || dp[i-2]=='1')
		{
			dp[i] += dp[i-2];
		}
	}

	return dp[n];

}
