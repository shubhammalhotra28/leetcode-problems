/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        
        vector<int> answer;
        
        postorderTraversal(root,answer);
        
        return answer;
        
    }
    
    private :
    void postorderTraversal(TreeNode* root, vector<int>& answer)
    {
        if(root==NULL)
            return;
        
        postorderTraversal(root->left,answer);
        postorderTraversal(root->right,answer);
        answer.push_back(root->val);
    }
};
