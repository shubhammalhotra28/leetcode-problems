#include<iostream>
#include<vector>
#include<unordered_map>

using namespace std;

vector<int> TwoSum(vector<int> &nums,int target){
	
	unordered_map<int,int> map;
	vector<int> ans;

	for(int i = 0;i<nums.size();i++)
	{
		int diff = target-nums[i];
		if(map.count(diff))
		{
		
			ans.push_back(map[diff]);
			ans.push_back(i);
			
		}
	map[nums[i]] = i;
	}
return ans;

}


int main(){

	int n ;
	cin>>n;
	vector<int> arr;
	for(int i = 0;i<n;i++)
	{
		cin>>arr[i];
	}

	int target;
	cin>>target;

	vector<int> ans =  TwoSum(arr,target);

	for(int i = 0;i<ans.size();i++)
	{
		cout<<ans[i]<<" "<<endl;
	}

	//return 0;
}
