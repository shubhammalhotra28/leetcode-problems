# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    
        # preorder (Root left right)
        # inorder (left root right)
        
        preOrderLen = len(preorder)
        inOrderLen = len(inorder)
        
        if preOrderLen!=inOrderLen or inOrderLen == None or preOrderLen == None or preOrderLen==0 or inOrderLen==0 :
            return None
        
        root = TreeNode(preorder[0])
        rootData = root.val
        
        rootIndex = inorder.index(rootData)
        
        root.left = self.buildTree(preorder[1:rootIndex+1],inorder[:rootIndex])
        root.right = self.buildTree(preorder[rootIndex+1:],inorder[rootIndex+1:])
        
        return root
        
        
        
    
