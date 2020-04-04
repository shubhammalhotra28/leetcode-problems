/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

#include<queue>

class Solution {
public:
    Node* connect(Node* root) {
    
        if(root==NULL)
            return root;
        
        queue<Node*> q;
        q.push(root);
        
        while(!q.empty())
        {
            int size = q.size();
            for(int i = 0;i<size;i++)
            {
            
                Node* data = q.front();
            
                q.pop();
            
                if(i<size-1)
                {
                    data->next = q.front();
                    //q.pop();
                }
                if(data->left!=NULL)
                {
                    q.push(data->left);
                }
                if(data->right!=NULL)
                {
                    q.push(data->right);
                }
            
            }
            
           
        }
         return root;
    }
};
