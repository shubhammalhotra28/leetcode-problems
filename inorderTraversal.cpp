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
    vector<int> inorderTraversal(TreeNode* root) {
        
        vector<int> answer;
        
        inorderTraversal(root,answer);
        
        return answer;
        
    }
    private :
    
    void inorderTraversal(TreeNode* root,vector<int>& answer)
    {
        if(root==NULL) // if root is NULL return 
            return;
     
        inorderTraversal(root->left,answer); // go through the left subtree and returning though recursion
        answer.push_back(root->val); //. push the node of root to answer
        inorderTraversal(root->right,answer); // call recurssion on right subtree
    }
    
    
};
