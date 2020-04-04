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
    bool isSymmetric(TreeNode* root) {
        
        if(root==NULL)
            return true;
        return isSymmetricCheck(root->left,root->right);
        
    }
    
    private :
    bool isSymmetricCheck(TreeNode* left, TreeNode* right)
    {
        if(left==NULL)
        {
            if(right==NULL)
                return true;
            else
                return false;
        }
        else
        {
            if(right==NULL)
            {
                return false;
            }
            else
            {
                return (left->val==right->val) && isSymmetricCheck(left->left,right->right) && isSymmetricCheck(left->right,right->left);        
            }
        }
        
        
    }
};
