#include<iostream>
#include<vector>
#include<cmath>

using napespace std;

vector<vector<int>> mergeIntervals(vector<vector<int>>& intervals){

	int left = intervals[0][0];
	int right = intervals[0][1];
	vector<vector<int>> ans;
	

	for(int i = 1;i<intervals.size();i++)
	{
		if(intervals[i][0]<=right)
		{
			right = max(right,intervals[i][1]);
		
		}	
		else
		{
			ans.push_back({left,right});
			left = intervals[i][0];
			right = intervals[i][1];
		}	
	}
	ans.push_back({left,right});
return ans;

}


int main(){
}
