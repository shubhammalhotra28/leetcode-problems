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
    vector<vector<int>> levelOrder(TreeNode* root) {
        
        vector<vector<int>> answer;
        queue<TreeNode*> q;
        if(root!=NULL)
        {
            q.push(root);
        }
        TreeNode* curr;
        while(!q.empty())
        {
            int size = q.size();
            answer.push_back(vector<int>());
            for(int i = 0;i<size;i++)
                // traversing the same level
            {
            curr = q.front();
            q.pop();
            answer.back().push_back(curr->val);
            
            if(curr->left!=NULL)
            {
                q.push(curr->left);
            }
            if(curr->right!=NULL)
            {
                q.push(curr->right);
                
            }
            
            }
        }
        
        return answer;
        
        
    }
};
