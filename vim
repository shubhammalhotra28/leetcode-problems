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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        
        int size = inorder.size();
        
        return build_tree_helper(preorder,inorder,0,size-1,0,size-1);
        
    }
    
    TreeNode* build_tree_helper(vector<int>& preorder, vector<int>& inorder,int inS, int inE , int preS, int preE)
    {
        if(inS>inE)
            return NULL;
        
        int rootData = preorder[preS];
        
        
        int lPreS = preS+1;
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
        
        int lInS = inS;
        int lInE = rootIndex-1;
        int lPreE = (lInE-lInS)+lPreS;
        //int lPreS = 
        int rPreS = lPreE+1;
        int rPreE = preE;
        int rInS = rootIndex+1;
        int rInE = inE;
        
        TreeNode* root = new TreeNode(rootData);
        
        root->left = build_tree_helper(preorder,inorder,lInS,lInE,lPreS,lPreE);
        
        root->right = build_tree_helper(preorder,inorder,rInS,rInE,rInS,rInE);
        
        return root;
            
            
    }
};
