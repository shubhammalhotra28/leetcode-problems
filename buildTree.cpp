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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        
      int size = inorder.size();
        return buildTree_helper(inorder,postorder,0,size-1,0,size-1);
        
    }
    TreeNode* buildTree_helper(vector<int>& inorder, vector<int>& postorder, int inS,int inE, int posS,int posE)
    {
        if(inS>inE)
            return NULL;
        
        int rootData = postorder[posE];
        
        int lposS = posS;
        int rootIndex = -1;
        int i;
        
        for(i = inS;i<=inE;i++)
        {
            if(inorder[i]==rootData)
            {
                rootIndex = i;
                break;
                
            }
        }
        
        int linS = inS;
        int linE = rootIndex-1;
        int leftSubTreeLength = linE - linS + 1;
        int lposE = lposS+leftSubTreeLength-1; 
        int rinS = rootIndex+1;
        int rinE  =  inE;
        int rposS  =  linE+1;
        int rposE  =  posE-1;
        
        TreeNode* root = new TreeNode(rootData);
        
        root->left = buildTree_helper(inorder,postorder,linS,linE,lposS,lposE);
        
        root->right = buildTree_helper(inorder,postorder,rinS,rinE,rposS,rposE);
        
        return root;
            
            
    }
};
