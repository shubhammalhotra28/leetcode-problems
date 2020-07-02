/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        
        if(nums.size()==0)
            return NULL;
        return constructTreeFromArray(nums,0,nums.size()-1);
        
    }
    public :
    TreeNode* constructTreeFromArray(vector<int> nums,int left,int right)
    {
        if(left>right)
            return NULL;
        int midpoint = left+(right-left)/2;
        cout<<left+(right-left)/2<<endl;
        TreeNode* node = new TreeNode(nums[midpoint]);
        node->left = constructTreeFromArray(nums,left,midpoint-1);
        node->right = constructTreeFromArray(nums,midpoint+1,right);
        
        return node;
    }
};










/*


TreeNode* sortedArrayToBST(vector<int>& nums){

	if(nums.size()==0)
	{
		return NULL;
	}

	return construct(nums,0,nums.size()-1);

}

TreeNode* construct(vector<int>& nums,int left,int right){


	if(left>right)
	{
		return NULL;
	}
	
	int midpoint = left+(right-left)/2;
	TreeNode* root = new TreeNode(nums[midpoint]);

	root->left = construct(nums,left,midpoint-1);
	root->right = construct(nums,midpoint+1,right);

	return root;

}*/
