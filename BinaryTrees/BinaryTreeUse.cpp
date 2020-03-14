#include<iostream>
#include<queue>
#include "BinaryTreeNode.h"
using namespace std;

pair<int,int> heightDiameter(BinaryTreeNode<int>* root)
{
	if(root==NULL)
	{
		pair<int,int> p;
		p.first = 0;
		p.second = 0;
		return p;
	}
	pair<int,int> leftAns = heightDiameter(root->left);
	pair<int,int> rightAns = heightDiameter(root->right);
	int ld = leftAns.second;
	int lh = leftAns.first;
	int rd = rightAns.second;
	int rh = rightAns.first;

	int height = 1+max(lh,rh);
	
	int diameter = max(lh+rh,max(ld,rd));
	
	pair<int,int> p;
	p.first = height;
	p.second = diameter;

	return p;
	
}









void printTree(BinaryTreeNode<int>* root){

	if(root==NULL)
	{
		return;
	}

	cout<<root->data<<":";

	if(root->left!=NULL)
	{
		cout<<"L"<<root->left->data;
	}
	if(root->right!=NULL)
	{
		cout<<"R"<<root->right->data;
	}
	
	cout<<endl;
	printTree(root->left);
	printTree(root->right);
}


int height(BinaryTreeNode<int>* root)
{
	if(root==NULL)
	{
		return 0;
	}

	return 1+max(height(root->left),height(root->right));

}

int diameter(BinaryTreeNode<int>* root)
{
	if(root==NULL)
	{
		return 0;
	}
	int option1 = height(root->left)+height(root->right);
	int option2 = diameter(root->left);
	int option3 = diameter(root->right);
	return max(option1,max(option2,option3));
}





BinaryTreeNode<int>* buildTreeHelper(int *in,int *pre, int inS,int inE, int preS, int preE)
{
	
	if(inS>inE)
	{
		return NULL;
	}

	int rootData = pre[preS];
	// no duplicates, then only tree is possible
	



	int lPreS = preS+1;
	
	int rootIndex = -1;
	int i;
	for(i=inS;i<=inE;i++)
	{
		if(in[i]==rootData)
		{
			rootIndex = i;
			break;
		}
	}
	
	int lInS = inS;
	int lInE = rootIndex-1;
	int lPreE = lInE-lInS+lPreS;
	int rPreS = lPreE+1;
	int rPreE = preE;
	int rInS = rootIndex+1;
	int rInE = inE;

	BinaryTreeNode<int>* root = new BinaryTreeNode<int>(rootData);
	root->left = buildTreeHelper(in,pre,lInS,lInE,lPreS,lPreE);
	root->right = buildTreeHelper(in,pre,rInS,rInE,rPreS,rPreE);
	
	return root;
	
}



BinaryTreeNode<int>* buildTree(int *in,int *pre,int size)
{
	return buildTreeHelper(in,pre,0,size-1,0,size-1);
}







void inorder(BinaryTreeNode<int>* root)
{
	if(root==NULL)
	{
		return;
	
	}
	
	inorder(root->left);
	cout<<root->data<<" ";
	inorder(root->right);

}
void preorder(BinaryTreeNode<int>* root)
{
	if(root==NULL)
	{
		return;
	}

	cout<<root->data<<" ";
	preorder(root->left);
	preorder(root->right);		

}


int numNodes(BinaryTreeNode<int>* root)
{
	if(root==NULL)
	{
		return 0;
	}
	
	return numNodes(root->left)+numNodes(root->right)+1;

}

BinaryTreeNode<int>* takeInput(){

	int rootData;
	cout<<"enter data"<<endl;
	cin>>rootData;
	if(rootData==-1)
	{
		return NULL;
	}

	BinaryTreeNode<int>* root = new BinaryTreeNode<int>(rootData);
	BinaryTreeNode<int>* leftChild = takeInput();
	BinaryTreeNode<int>* rightChild = takeInput();

	root->left = leftChild;
	root->right = rightChild;

	return root;
}


BinaryTreeNode<int>* takeInputLevelWise(){

	int rootData;
	cout<<"enter rootData"<<endl;
	cin>>rootData;

	if(rootData==-1)
	{
		return NULL;
	}
	BinaryTreeNode<int>* root = new BinaryTreeNode<int>(rootData);

	queue<BinaryTreeNode<int>*> pendingNodes;

	pendingNodes.push(root);

	while(pendingNodes.size()!=0)
	{
		BinaryTreeNode<int>* front = pendingNodes.front();
		pendingNodes.pop();
		cout<<"enter left child of"<<front->data<<endl;
		int leftChild;
		cin>>leftChild;
		if(leftChild!=-1)
		{
			BinaryTreeNode<int>* child = new BinaryTreeNode<int>(leftChild);
			front->left = child;
			pendingNodes.push(child);	
		}		
		cout<<"enter right child of"<<front->data<<endl;
                int rightChild;
                cin>>rightChild;
                if(rightChild!=-1)
                {
                        BinaryTreeNode<int>* child = new BinaryTreeNode<int>(rightChild);
                        front->right = child;
                        pendingNodes.push(child);
                }
	
	}

	return root;

}





int main(){
	// 1 2 3 4 5 6 7 -1 -1 -1 -1 8 9 -1 -1 -1 -1 -1 -1
	
	/*BinaryTreeNode<int>* root = new BinaryTreeNode<int>(1);
	BinaryTreeNode<int>* node1 = new BinaryTreeNode<int>(2);
	BinaryTreeNode<int>* node2 = new BinaryTreeNode<int>(3);
	
	root->left = node1;
	root->right = node2;
*/


	/*int in[] = {4,2,5,1,8,6,9,3,7};
	int pre[] = {1,2,4,5,3,6,8,9,7};
	BinaryTreeNode<int>* root = buildTree(in,pre,9);
	printTree(root);
	delete root;
*/
	/*
	BinaryTreeNode<int>* root = takeInputLevelWise();
	printTree(root);

	cout<<"num of nodes"<<numNodes(root)<<endl;
	cout<<"*********************************************"<<endl;
	inorder(root);
	cout<<"*********************************************"<<endl;
	preorder(root);

*/
	


	BinaryTreeNode<int>* root = takeInputLevelWise();
	printTree(root);
	cout<<endl;
	inorder(root);
	cout<<endl;
	pair<int,int> p = heightDiameter(root);
	cout<<"height"<< p.first<<endl;
	cout<<"diamter"<<p.second<<endl;

	delete root;

	

}
